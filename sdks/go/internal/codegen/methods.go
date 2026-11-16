package codegen

import (
	"fmt"
	"strings"
)

type methodEntry struct {
	name string
	op   *operation
}

func resolveMethodNames(group *resourceGroup) ([]methodEntry, error) {
	entries := make([]methodEntry, 0, len(group.operations))
	for _, op := range group.operations {
		entries = append(entries, methodEntry{name: operationMethodName(op.id, group.servicePascal, group.resourcePascal), op: op})
	}

	counts := countNames(entries)
	for index := range entries {
		entry := &entries[index]
		if counts[entry.name] <= 1 {
			continue
		}
		if entry.op.kind == responseList {
			if entry.name == "read" || entry.name == "get" {
				entry.name = "list"
			} else {
				entry.name = "list" + upperFirst(entry.name)
			}
		} else if strings.Contains(entry.op.id, pluralize(group.resourcePascal)) {
			entry.name = pluralize(entry.name)
		}
	}

	counts = countNames(entries)
	for index := range entries {
		if counts[entries[index].name] > 1 {
			entries[index].name = lowerFirst(entries[index].op.id)
		}
	}

	seen := map[string]bool{}
	for index := range entries {
		goName := upperFirst(entries[index].name)
		if seen[goName] {
			return nil, fmt.Errorf("two operations in %s - %s both generate the method %s", group.service, group.resource, goName)
		}
		seen[goName] = true
		entries[index].name = goName
		entries[index].op.methodName = goName
	}
	return entries, nil
}

func countNames(entries []methodEntry) map[string]int {
	counts := map[string]int{}
	for _, entry := range entries {
		counts[entry.name]++
	}
	return counts
}

func serviceFieldName(group *resourceGroup) string {
	return nonAlphanumeric.ReplaceAllString(pluralize(group.resourcePascal), "")
}

type operationTypes struct {
	bodyParam    string
	queryParam   string
	headersParam string
	result       string
	resultKind   typeKind
	listItem     string
}

func (b *typeBuilder) operationTypes(op *operation, base string) (operationTypes, error) {
	var types operationTypes
	if len(op.headers) > 0 {
		types.headersParam = b.claimName(base + "Headers")
	}
	if op.body != nil {
		typ, _, err := b.named(op.body, base+"Request")
		if err != nil {
			return types, err
		}
		types.bodyParam = typ.expr()
		if typ.pointable() {
			types.bodyParam = "*" + types.bodyParam
		}
	}
	if len(op.query) > 0 {
		shape := newObjectShape()
		for _, parameter := range op.query {
			shape.add(parameter.name, parameter.schema, parameter.required)
		}
		before := len(b.defs)
		typ, err := b.structFrom(shape, base+"Query", 0)
		if err != nil {
			return types, err
		}
		types.queryParam = b.aliasShared(typ, base+"Query", before).expr()
		if typ.pointable() {
			types.queryParam = "*" + types.queryParam
		}
	}
	switch op.kind {
	case responseList:
		typ, _, err := b.named(op.result, base+"Item")
		if err != nil {
			return types, err
		}
		types.listItem = typ.expr()
	case responseEnvelope, responseBody:
		typ, _, err := b.named(op.result, base+"Response")
		if err != nil {
			return types, err
		}
		types.resultKind = typ.kind
		if typ.kind != kindNull {
			types.result = typ.expr()
		}
	}
	return types, nil
}
