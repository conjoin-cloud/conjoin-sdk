package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/conjoin-cloud/conjoin-sdk/sdks/go/internal/codegen"
)

func main() {
	specDir := flag.String("spec", "../../spec", "directory that holds openapi.json and openapi-frontend.json")
	outputDir := flag.String("out", ".", "root directory of the Go module")
	flag.Parse()

	summaries, err := codegen.Generate(codegen.DefaultDocuments(*specDir, *outputDir))
	if err != nil {
		fmt.Fprintln(os.Stderr, "generate:", err)
		os.Exit(1)
	}
	for _, summary := range summaries {
		fmt.Println(summary)
	}
}
