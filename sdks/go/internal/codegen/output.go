package codegen

import (
	"errors"
	"fmt"
	"go/format"
	"os"
	"path/filepath"
	"slices"
	"strconv"
	"strings"
)

const (
	modulePath         = "github.com/conjoin-cloud/conjoin-sdk/sdks/go"
	maxFileLines       = 399
	chunkLineBudget    = 340
	generatedSuffix    = "_gen.go"
	serviceImportBlock = "import (\n\t\"context\"\n\n\tconjoin \"" + modulePath + "\"\n)\n\n"
)

type generatedFile struct {
	path    string
	content []byte
}

func countLines(text string) int {
	return strings.Count(text, "\n")
}

func chunkDeclarations(declarations []string) [][]string {
	var chunks [][]string
	var current []string
	lines := 0
	for _, declaration := range declarations {
		size := countLines(declaration) + 1
		if len(current) > 0 && lines+size > chunkLineBudget {
			chunks = append(chunks, current)
			current, lines = nil, 0
		}
		current = append(current, declaration)
		lines += size
	}
	if len(current) > 0 {
		chunks = append(chunks, current)
	}
	return chunks
}

func formatFile(path, source string) (generatedFile, error) {
	formatted, err := format.Source([]byte(source))
	if err != nil {
		return generatedFile{}, fmt.Errorf("%s does not parse as Go: %w", path, err)
	}
	if lines := countLines(string(formatted)); lines > maxFileLines {
		return generatedFile{}, fmt.Errorf("%s has %d lines, over the %d line limit", path, lines, maxFileLines)
	}
	return generatedFile{path: path, content: formatted}, nil
}

func chunkedFiles(directory, stem string, declarations []string, headerFor func(start, end int) string) ([]generatedFile, error) {
	var files []generatedFile
	start := 0
	for index, chunk := range chunkDeclarations(declarations) {
		name := stem
		if index > 0 {
			name += "_" + strconv.Itoa(index+1)
		}
		end := start + len(chunk)
		file, err := formatFile(filepath.Join(directory, name+generatedSuffix), headerFor(start, end)+strings.Join(chunk, "\n"))
		if err != nil {
			return nil, err
		}
		files = append(files, file)
		start = end
	}
	return files, nil
}

func renderModelFiles(directory, stem, header string, defs []*structDef) ([]generatedFile, error) {
	declarations := make([]string, 0, len(defs))
	for _, def := range defs {
		declarations = append(declarations, renderStruct(def))
	}
	return chunkedFiles(directory, stem, declarations, func(start, end int) string {
		for _, def := range defs[start:end] {
			if slices.ContainsFunc(def.fields, structField.usesNullable) {
				return header + "import conjoin \"" + modulePath + "\"\n\n"
			}
		}
		return header
	})
}

func isGeneratedPackageDirectory(directory string) (bool, error) {
	entries, err := os.ReadDir(directory)
	if err != nil {
		return false, err
	}
	for _, entry := range entries {
		if entry.IsDir() || !strings.HasSuffix(entry.Name(), generatedSuffix) {
			return false, nil
		}
	}
	return true, nil
}

func removeGeneratedPackages(root string, keep []string) error {
	entries, err := os.ReadDir(root)
	if errors.Is(err, os.ErrNotExist) {
		return nil
	}
	if err != nil {
		return err
	}
	for _, entry := range entries {
		if !entry.IsDir() || slices.Contains(keep, entry.Name()) {
			continue
		}
		directory := filepath.Join(root, entry.Name())
		generated, err := isGeneratedPackageDirectory(directory)
		if err != nil {
			return err
		}
		if generated {
			if err := os.RemoveAll(directory); err != nil {
				return err
			}
		}
	}
	return nil
}

func writeFiles(files []generatedFile) error {
	seen := map[string]bool{}
	for _, file := range files {
		if seen[file.path] {
			return fmt.Errorf("two generated files share the path %s", file.path)
		}
		seen[file.path] = true
	}
	for _, file := range files {
		if err := os.MkdirAll(filepath.Dir(file.path), 0o755); err != nil {
			return err
		}
		if err := os.WriteFile(file.path, file.content, 0o644); err != nil {
			return err
		}
	}
	return nil
}
