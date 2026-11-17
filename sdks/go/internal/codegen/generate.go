package codegen

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"slices"
)

var packageNamePattern = regexp.MustCompile(`^[a-z][a-z0-9]*$`)

type Document struct {
	SpecFile  string
	OutputDir string
}

type Summary struct {
	SpecFile   string
	Operations int
	Packages   int
	Files      int
}

type servicePackage struct {
	name    string
	groups  []*resourceGroup
	builder *typeBuilder
}

func Generate(documents []Document) ([]Summary, error) {
	summaries := make([]Summary, 0, len(documents))
	for _, document := range documents {
		summary, err := generateDocument(document)
		if err != nil {
			return nil, fmt.Errorf("%s: %w", document.SpecFile, err)
		}
		summaries = append(summaries, summary)
	}
	return summaries, nil
}

func generateDocument(source Document) (Summary, error) {
	data, err := os.ReadFile(source.SpecFile)
	if err != nil {
		return Summary{}, err
	}
	root, err := parseDocument(data)
	if err != nil {
		return Summary{}, err
	}
	doc := &document{root: root}
	groups, err := doc.collectGroups()
	if err != nil {
		return Summary{}, err
	}

	var packages []*servicePackage
	byName := map[string]*servicePackage{}
	operations := 0
	for _, group := range groups {
		if !packageNamePattern.MatchString(group.service) {
			return Summary{}, fmt.Errorf("the service %q cannot be a Go package name", group.service)
		}
		pkg, exists := byName[group.service]
		if !exists {
			pkg = &servicePackage{name: group.service, builder: newTypeBuilder(doc)}
			byName[group.service] = pkg
			packages = append(packages, pkg)
		}
		pkg.groups = append(pkg.groups, group)
		operations += len(group.operations)
	}

	var files []generatedFile
	keep := []string{"internal", "frontend"}
	for _, pkg := range packages {
		packageFiles, err := renderPackage(pkg, filepath.Join(source.OutputDir, pkg.name))
		if err != nil {
			return Summary{}, fmt.Errorf("package %s: %w", pkg.name, err)
		}
		files = append(files, packageFiles...)
	}
	if err := removeGeneratedPackages(source.OutputDir, keep); err != nil {
		return Summary{}, err
	}
	if err := writeFiles(files); err != nil {
		return Summary{}, err
	}
	return Summary{SpecFile: filepath.Base(source.SpecFile), Operations: operations, Packages: len(packages), Files: len(files)}, nil
}

func renderPackage(pkg *servicePackage, directory string) ([]generatedFile, error) {
	baseNames := map[string]string{}
	methods := map[*resourceGroup]map[*operation]string{}
	for _, group := range pkg.groups {
		entries, err := resolveMethodNames(group)
		if err != nil {
			return nil, err
		}
		methods[group] = map[*operation]string{}
		for _, entry := range entries {
			base := operationTypeBase(entry.op.id, group.servicePascal)
			if other, taken := baseNames[base]; taken {
				return nil, fmt.Errorf("the operations %s and %s both generate the types %s", other, entry.op.id, base)
			}
			baseNames[base] = entry.op.id
			methods[group][entry.op] = base
		}
	}

	var files []generatedFile
	var fields []string
	header := "package " + pkg.name + "\n\n"
	for _, group := range pkg.groups {
		field := serviceFieldName(group)
		if slices.Contains(fields, field) {
			return nil, fmt.Errorf("two resources both generate the service %s", field)
		}
		fields = append(fields, field)
		serviceType := field + "Service"

		pkg.builder.owner = field
		definitionsBefore := len(pkg.builder.defs)
		declarations := []string{renderServiceType(serviceType)}
		for _, op := range group.operations {
			types, err := pkg.builder.operationTypes(op, methods[group][op])
			if err != nil {
				return nil, fmt.Errorf("%s: %w", op.id, err)
			}
			declarations = append(declarations, renderMethod(serviceType, op, types))
		}

		stem := snakeCase(group.resource)
		serviceFiles, err := chunkedFiles(directory, stem+"_service", declarations, func(int, int) string { return header + serviceImportBlock })
		if err != nil {
			return nil, err
		}
		files = append(files, serviceFiles...)

		modelFiles, err := renderModelFiles(directory, stem+"_models", header, pkg.builder.defs[definitionsBefore:])
		if err != nil {
			return nil, err
		}
		files = append(files, modelFiles...)
	}

	slices.Sort(fields)
	clientFile, err := formatFile(filepath.Join(directory, "package"+generatedSuffix), renderPackageClient(pkg.name, fields))
	if err != nil {
		return nil, err
	}
	return append(files, clientFile), nil
}

func DefaultDocuments(specDir, outputDir string) []Document {
	return []Document{
		{SpecFile: filepath.Join(specDir, "openapi.json"), OutputDir: outputDir},
		{SpecFile: filepath.Join(specDir, "openapi-frontend.json"), OutputDir: filepath.Join(outputDir, "frontend")},
	}
}

func (s Summary) String() string {
	return fmt.Sprintf("%s: %d operations in %d packages and %d files", s.SpecFile, s.Operations, s.Packages, s.Files)
}
