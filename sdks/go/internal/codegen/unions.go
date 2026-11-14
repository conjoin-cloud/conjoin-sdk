package codegen

import "fmt"

type objectShape struct {
	keys     []string
	schemas  map[string][]any
	seen     map[string]map[string]bool
	required map[string]bool
}

func newObjectShape() *objectShape {
	return &objectShape{schemas: map[string][]any{}, seen: map[string]map[string]bool{}, required: map[string]bool{}}
}

func (s *objectShape) add(key string, schema any, required bool) {
	if _, exists := s.schemas[key]; !exists {
		s.keys = append(s.keys, key)
		s.seen[key] = map[string]bool{}
	}
	if fingerprint := canonical(schema); !s.seen[key][fingerprint] {
		s.seen[key][fingerprint] = true
		s.schemas[key] = append(s.schemas[key], schema)
	}
	if required {
		s.required[key] = true
	}
}

func (s *objectShape) merge(other *objectShape, keepRequired bool) {
	for _, key := range other.keys {
		for _, schema := range other.schemas[key] {
			s.add(key, schema, keepRequired && other.required[key])
		}
	}
}

func (s *objectShape) fieldSchema(key string) any {
	schemas := s.schemas[key]
	if len(schemas) == 1 {
		return schemas[0]
	}
	return &object{keys: []string{"anyOf"}, values: map[string]any{"anyOf": schemas}}
}

func unionBranches(s *object) []any {
	if branches := s.list("oneOf"); branches != nil {
		return branches
	}
	return s.list("anyOf")
}

func isPureUnion(s *object) bool {
	return unionBranches(s) != nil && !s.has("type") && !s.has("properties") && !s.has("allOf") && !s.has("const") && !s.has("enum")
}

func (b *typeBuilder) flattenBranches(branches []any, depth int) ([]*object, bool, error) {
	if depth > maxSchemaDepth {
		return nil, false, fmt.Errorf("a union nests deeper than the generator allows")
	}
	var flat []*object
	nullable := false
	for _, raw := range branches {
		branch, err := b.doc.resolve(raw)
		if err != nil {
			return nil, false, err
		}
		if branch == nil {
			flat = append(flat, &object{values: map[string]any{}})
			continue
		}
		if isPureUnion(branch) {
			nested, nestedNullable, err := b.flattenBranches(unionBranches(branch), depth+1)
			if err != nil {
				return nil, false, err
			}
			flat = append(flat, nested...)
			nullable = nullable || nestedNullable
			continue
		}
		if typeName, _ := schemaTypes(branch); typeName == "null" && !branch.has("properties") {
			nullable = true
			continue
		}
		if branch.has("const") && branch.get("const") == nil {
			nullable = true
			continue
		}
		flat = append(flat, branch)
	}
	return flat, nullable, nil
}

func branchClass(s *object) string {
	if s.has("const") {
		return kindClass(valueKind(s.get("const")))
	}
	if s.has("properties") || s.has("allOf") {
		return "object"
	}
	typeName, _ := schemaTypes(s)
	if typeName == "" && s.has("enum") {
		return kindClass(enumKind(s.list("enum")))
	}
	switch typeName {
	case "string", "boolean", "array":
		return typeName
	case "integer":
		return "integer"
	case "number":
		return "number"
	case "object":
		return "map"
	}
	return "any"
}

func kindClass(kind typeKind) string {
	switch kind {
	case kindString:
		return "string"
	case kindBool:
		return "boolean"
	case kindInt:
		return "integer"
	case kindFloat:
		return "number"
	}
	return "any"
}

func (b *typeBuilder) union(raw []any, name string, depth int) (*goType, bool, error) {
	branches, nullable, err := b.flattenBranches(raw, depth)
	if err != nil {
		return nil, false, err
	}
	switch len(branches) {
	case 0:
		return &goType{kind: kindAny}, true, nil
	case 1:
		typ, branchNullable, err := b.build(branches[0], name, depth+1)
		return typ, nullable || branchNullable, err
	}

	classes := map[string]bool{}
	for _, branch := range branches {
		classes[branchClass(branch)] = true
	}
	only := func(allowed ...string) bool {
		for class := range classes {
			matched := false
			for _, candidate := range allowed {
				matched = matched || class == candidate
			}
			if !matched {
				return false
			}
		}
		return true
	}

	switch {
	case only("object"):
		shape := newObjectShape()
		for _, branch := range branches {
			branchShape, err := b.shapeOf(branch, false, depth+1)
			if err != nil {
				return nil, false, err
			}
			shape.merge(branchShape, false)
		}
		typ, err := b.structFrom(shape, name, depth)
		return typ, nullable, err
	case only("string"):
		return &goType{kind: kindString}, nullable, nil
	case only("integer"):
		return &goType{kind: kindInt}, nullable, nil
	case only("integer", "number"):
		return &goType{kind: kindFloat}, nullable, nil
	case only("boolean"):
		return &goType{kind: kindBool}, nullable, nil
	case only("array"):
		items := make([]any, 0, len(branches))
		for _, branch := range branches {
			items = append(items, branch.get("items"))
		}
		elem, _, err := b.union(items, name+"Item", depth+1)
		if err != nil {
			return nil, false, err
		}
		return &goType{kind: kindSlice, elem: elem}, nullable, nil
	}
	return &goType{kind: kindAny}, nullable, nil
}

func (b *typeBuilder) shapeOf(s *object, strict bool, depth int) (*objectShape, error) {
	if depth > maxSchemaDepth {
		return nil, fmt.Errorf("an object schema nests deeper than the generator allows")
	}
	shape := newObjectShape()
	required := map[string]bool{}
	if strict {
		for _, entry := range s.list("required") {
			if key, ok := entry.(string); ok {
				required[key] = true
			}
		}
	}
	properties := s.object("properties")
	for _, key := range properties.orderedKeys() {
		shape.add(key, properties.get(key), required[key])
	}
	for _, raw := range s.list("allOf") {
		part, err := b.doc.resolve(raw)
		if err != nil {
			return nil, err
		}
		if part == nil {
			continue
		}
		partShape, err := b.shapeOf(part, strict, depth+1)
		if err != nil {
			return nil, err
		}
		shape.merge(partShape, strict)
	}
	if branches := unionBranches(s); branches != nil {
		flat, _, err := b.flattenBranches(branches, depth+1)
		if err != nil {
			return nil, err
		}
		for _, branch := range flat {
			branchShape, err := b.shapeOf(branch, false, depth+1)
			if err != nil {
				return nil, err
			}
			shape.merge(branchShape, false)
		}
	}
	return shape, nil
}
