package codegen

import (
	"encoding/json"
	"fmt"
	"slices"
	"strconv"
	"strings"
)

type typeKind int

const (
	kindAny typeKind = iota
	kindNull
	kindString
	kindInt
	kindFloat
	kindBool
	kindStruct
	kindSlice
	kindMap
)

const maxSchemaDepth = 64

type goType struct {
	kind typeKind
	elem *goType
	def  *structDef
}

type structField struct {
	goName   string
	jsonName string
	typ      *goType
	required bool
	nullable bool
}

type structDef struct {
	name      string
	fields    []structField
	signature string
	owner     string
	target    string
}

type typeBuilder struct {
	doc         *document
	defs        []*structDef
	bySignature map[string]*structDef
	names       map[string]bool
	owner       string
}

func newTypeBuilder(doc *document) *typeBuilder {
	return &typeBuilder{doc: doc, bySignature: map[string]*structDef{}, names: map[string]bool{}}
}

func (t *goType) expr() string {
	switch t.kind {
	case kindString:
		return "string"
	case kindInt:
		return "int64"
	case kindFloat:
		return "float64"
	case kindBool:
		return "bool"
	case kindStruct:
		return t.def.name
	case kindSlice:
		return "[]" + t.elem.expr()
	case kindMap:
		return "map[string]" + t.elem.expr()
	}
	return "any"
}

func (t *goType) pointable() bool {
	switch t.kind {
	case kindString, kindInt, kindFloat, kindBool, kindStruct:
		return true
	}
	return false
}

func (f structField) usesNullable() bool {
	return !f.required && f.nullable && f.typ.kind != kindAny && f.typ.kind != kindNull
}

func (f structField) expr() string {
	if f.usesNullable() {
		return "conjoin.Nullable[" + f.typ.expr() + "]"
	}
	if (!f.required || f.nullable) && f.typ.pointable() {
		return "*" + f.typ.expr()
	}
	return f.typ.expr()
}

func (f structField) tag() string {
	if f.required {
		return "`json:\"" + f.jsonName + "\"`"
	}
	return "`json:\"" + f.jsonName + ",omitzero\"`"
}

func (b *typeBuilder) claimName(name string) string {
	candidate := name
	for suffix := 2; b.names[candidate]; suffix++ {
		candidate = name + strconv.Itoa(suffix)
	}
	b.names[candidate] = true
	return candidate
}

func isValidJSONKey(key string) bool {
	if key == "" {
		return false
	}
	for _, r := range key {
		if r == '"' || r == '\\' || r == ',' || r == '`' || r < 0x20 || r == 0x7f {
			return false
		}
	}
	return true
}

func scalarKind(typeName string) (typeKind, bool) {
	switch typeName {
	case "string":
		return kindString, true
	case "integer":
		return kindInt, true
	case "number":
		return kindFloat, true
	case "boolean":
		return kindBool, true
	case "null":
		return kindNull, true
	}
	return kindAny, false
}

func schemaTypes(s *object) (string, bool) {
	switch typed := s.get("type").(type) {
	case string:
		return typed, typed == "null"
	case []any:
		chosen, nullable := "", false
		for _, entry := range typed {
			name, _ := entry.(string)
			if name == "null" {
				nullable = true
			} else if chosen == "" {
				chosen = name
			}
		}
		if chosen == "" && nullable {
			chosen = "null"
		}
		return chosen, nullable
	}
	return "", false
}

func valueKind(value any) typeKind {
	switch typed := value.(type) {
	case string:
		return kindString
	case bool:
		return kindBool
	case nil:
		return kindNull
	case json.Number:
		if strings.ContainsAny(typed.String(), ".eE") {
			return kindFloat
		}
		return kindInt
	}
	return kindAny
}

func enumKind(values []any) typeKind {
	kind := kindNull
	for _, value := range values {
		next := valueKind(value)
		switch {
		case next == kindNull:
		case kind == kindNull:
			kind = next
		case kind != next:
			return kindAny
		}
	}
	return kind
}

func (b *typeBuilder) build(schema any, name string, depth int) (*goType, bool, error) {
	if depth > maxSchemaDepth {
		return nil, false, fmt.Errorf("the schema behind %s nests deeper than the generator allows", name)
	}
	s, err := b.doc.resolve(schema)
	if err != nil || s == nil {
		return &goType{kind: kindAny}, false, err
	}
	if s.has("const") {
		kind := valueKind(s.get("const"))
		return &goType{kind: kind}, kind == kindNull, nil
	}
	if s.has("properties") || s.has("allOf") {
		shape, err := b.shapeOf(s, true, depth)
		if err != nil {
			return nil, false, err
		}
		typ, err := b.structFrom(shape, name, depth)
		return typ, false, err
	}
	if branches := unionBranches(s); branches != nil {
		return b.union(branches, name, depth)
	}

	typeName, nullable := schemaTypes(s)
	if typeName == "" && s.has("enum") {
		kind := enumKind(s.list("enum"))
		return &goType{kind: kind}, nullable || kind == kindNull, nil
	}
	if kind, isScalar := scalarKind(typeName); isScalar {
		return &goType{kind: kind}, nullable || kind == kindNull, nil
	}
	switch typeName {
	case "array":
		elem, _, err := b.build(s.get("items"), name+"Item", depth+1)
		if err != nil {
			return nil, false, err
		}
		return &goType{kind: kindSlice, elem: elem}, nullable, nil
	case "object":
		elem := &goType{kind: kindAny}
		if additional, ok := s.get("additionalProperties").(*object); ok {
			elem, _, err = b.build(additional, name+"Value", depth+1)
			if err != nil {
				return nil, false, err
			}
		}
		return &goType{kind: kindMap, elem: elem}, nullable, nil
	}
	return &goType{kind: kindAny}, nullable, nil
}

func (b *typeBuilder) structFrom(shape *objectShape, name string, depth int) (*goType, error) {
	fields := make([]structField, 0, len(shape.keys))
	used := map[string]bool{}
	var signature strings.Builder
	for _, key := range shape.keys {
		if !isValidJSONKey(key) {
			return nil, fmt.Errorf("the property %q under %s cannot be a JSON struct tag", key, name)
		}
		goName := goIdentifier(key)
		for suffix := 2; used[goName]; suffix++ {
			goName = goIdentifier(key) + strconv.Itoa(suffix)
		}
		used[goName] = true
		typ, nullable, err := b.build(shape.fieldSchema(key), name+goName, depth+1)
		if err != nil {
			return nil, err
		}
		field := structField{goName: goName, jsonName: key, typ: typ, required: shape.required[key], nullable: nullable}
		fields = append(fields, field)
		fmt.Fprintf(&signature, "%s %s %s;", field.goName, field.expr(), field.tag())
	}
	if len(fields) == 0 {
		return &goType{kind: kindMap, elem: &goType{kind: kindAny}}, nil
	}
	if existing, found := b.bySignature[signature.String()]; found {
		return &goType{kind: kindStruct, def: existing}, nil
	}
	def := &structDef{name: b.claimName(name), fields: fields, signature: signature.String(), owner: b.owner}
	b.bySignature[def.signature] = def
	b.defs = append(b.defs, def)
	return &goType{kind: kindStruct, def: def}, nil
}

func (b *typeBuilder) named(schema any, name string) (*goType, bool, error) {
	before := len(b.defs)
	typ, nullable, err := b.build(schema, name, 0)
	if err != nil {
		return nil, false, err
	}
	return b.aliasShared(typ, name, before), nullable, nil
}

func (b *typeBuilder) aliasShared(typ *goType, name string, before int) *goType {
	if typ.kind != kindStruct || slices.Contains(b.defs[before:], typ.def) {
		return typ
	}
	alias := &structDef{name: b.claimName(name), owner: b.owner, target: typ.def.name}
	b.defs = append(b.defs, alias)
	return &goType{kind: kindStruct, def: alias}
}
