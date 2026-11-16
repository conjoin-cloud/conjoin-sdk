package codegen

import (
	"fmt"
	"slices"
	"strings"
)

const (
	authDefault             = ""
	authNone                = "conjoin.AuthNone"
	authBearerToken         = "conjoin.AuthBearerToken"
	authPublishableKey      = "conjoin.AuthPublishableKey"
	authSession             = "conjoin.AuthSession"
	portalTicketHeaderName  = "conjoinPortalTicketHeader"
	portalTicketFieldName   = "PortalTicket"
	portalTicketQueryScheme = "conjoinPortalTicketQuery"
)

type securityGroup struct {
	auth           string
	sendsPortalKey bool
	schemes        []string
}

var securityGroups = []securityGroup{
	{auth: authDefault, schemes: []string{"conjoinApiKey"}},
	{auth: authBearerToken, schemes: []string{"scimBearer"}},
	{auth: authPublishableKey, schemes: []string{"conjoinPublishableKey"}},
	{auth: authSession, schemes: []string{"conjoinSessionBearer", "conjoinSessionCookie"}},
	{auth: authNone, sendsPortalKey: true, schemes: []string{portalTicketHeaderName, portalTicketQueryScheme}},
}

func resolveSecurity(op *object, operationID string) (securityGroup, error) {
	if !op.has("security") {
		return securityGroup{auth: authDefault}, nil
	}
	var schemes []string
	for _, requirement := range op.list("security") {
		entry, _ := requirement.(*object)
		schemes = append(schemes, entry.orderedKeys()...)
	}
	if len(schemes) == 0 {
		return securityGroup{auth: authNone}, nil
	}
	for _, group := range securityGroups {
		if allIn(schemes, group.schemes) {
			return group, nil
		}
	}
	return securityGroup{}, fmt.Errorf("%s declares the security schemes %s, which no SDK call supports", operationID, strings.Join(schemes, ", "))
}

func allIn(values, allowed []string) bool {
	for _, value := range values {
		if !slices.Contains(allowed, value) {
			return false
		}
	}
	return true
}

func (d *document) portalTicketHeader(operationID string) (declaredHeader, error) {
	scheme := d.root.object("components").object("securitySchemes").object(portalTicketHeaderName)
	name := scheme.text("name")
	if scheme.text("in") != "header" || name == "" {
		return declaredHeader{}, fmt.Errorf("%s needs %s, which the document does not declare as a header", operationID, portalTicketHeaderName)
	}
	return declaredHeader{name: name, field: portalTicketFieldName, required: true, credential: true}, nil
}
