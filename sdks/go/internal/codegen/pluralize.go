package codegen

import (
	"regexp"
	"strings"
)

var uncountableWords = map[string]bool{
	"adulthood": true, "advice": true, "agenda": true, "aid": true, "aircraft": true, "alcohol": true,
	"ammo": true, "analytics": true, "anime": true, "athletics": true, "audio": true, "bison": true,
	"blood": true, "bream": true, "buffalo": true, "butter": true, "carp": true, "cash": true,
	"chassis": true, "chess": true, "clothing": true, "cod": true, "commerce": true, "cooperation": true,
	"corps": true, "debris": true, "diabetes": true, "digestion": true, "elk": true, "energy": true,
	"equipment": true, "excretion": true, "expertise": true, "firmware": true, "flounder": true, "fun": true,
	"gallows": true, "garbage": true, "graffiti": true, "hardware": true, "headquarters": true, "health": true,
	"herpes": true, "highjinks": true, "homework": true, "housework": true, "information": true, "jeans": true,
	"justice": true, "kudos": true, "labour": true, "literature": true, "machinery": true, "mackerel": true,
	"mail": true, "media": true, "mews": true, "moose": true, "music": true, "mud": true,
	"manga": true, "news": true, "only": true, "personnel": true, "pike": true, "plankton": true,
	"pliers": true, "police": true, "pollution": true, "premises": true, "rain": true, "research": true,
	"rice": true, "salmon": true, "scissors": true, "series": true, "sewage": true, "shambles": true,
	"shrimp": true, "software": true, "staff": true, "swine": true, "tennis": true, "traffic": true,
	"transportation": true, "trout": true, "tuna": true, "wealth": true, "welfare": true, "whiting": true,
	"wildebeest": true, "wildlife": true, "you": true,
}

var uncountableRules = []*regexp.Regexp{
	regexp.MustCompile(`(?i)[^aeiou]ese$`),
	regexp.MustCompile(`(?i)deer$`),
	regexp.MustCompile(`(?i)fish$`),
	regexp.MustCompile(`(?i)measles$`),
	regexp.MustCompile(`(?i)o[iu]s$`),
	regexp.MustCompile(`(?i)pox$`),
	regexp.MustCompile(`(?i)sheep$`),
}

var irregularPlurals = map[string]string{
	"child": "children", "die": "dice", "echo": "echoes", "foot": "feet", "genus": "genera",
	"goose": "geese", "human": "humans", "man": "men", "ox": "oxen", "person": "people",
	"quiz": "quizzes", "tooth": "teeth", "woman": "women",
}

type pluralRule struct {
	pattern     *regexp.Regexp
	replacement string
}

var pluralRules = []pluralRule{
	{regexp.MustCompile(`(?i)m[ae]n$`), "men"},
	{regexp.MustCompile(`(?i)eaux$`), "${0}"},
	{regexp.MustCompile(`(?i)(child)(?:ren)?$`), "${1}ren"},
	{regexp.MustCompile(`(?i)(pe)(?:rson|ople)$`), "${1}ople"},
	{regexp.MustCompile(`(?i)\b((?:tit)?m|l)(?:ice|ouse)$`), "${1}ice"},
	{regexp.MustCompile(`(?i)(matr|cod|mur|sil|vert|ind|append)(?:ix|ex)$`), "${1}ices"},
	{regexp.MustCompile(`(?i)(x|ch|ss|sh|zz)$`), "${1}es"},
	{regexp.MustCompile(`(?i)([^ch][ieo][ln])ey$`), "${1}ies"},
	{regexp.MustCompile(`(?i)([^aeiouy]|qu)y$`), "${1}ies"},
	{regexp.MustCompile(`(?i)(?:(kni|wi|li)fe|(ar|l|ea|eo|oa|hoo)f)$`), "${1}${2}ves"},
	{regexp.MustCompile(`(?i)sis$`), "ses"},
	{regexp.MustCompile(`(?i)(apheli|hyperbat|periheli|asyndet|noumen|phenomen|criteri|organ|prolegomen|hedr|automat)(?:a|on)$`), "${1}a"},
	{regexp.MustCompile(`(?i)(agend|addend|millenni|dat|extrem|bacteri|desiderat|strat|candelabr|errat|ov|symposi|curricul|automat|quor)(?:a|um)$`), "${1}a"},
	{regexp.MustCompile(`(?i)(her|at|gr)o$`), "${1}oes"},
	{regexp.MustCompile(`(?i)(seraph|cherub)(?:im)?$`), "${1}im"},
	{regexp.MustCompile(`(?i)(alumn|alg|vertebr)(?:a|ae)$`), "${1}ae"},
	{regexp.MustCompile(`(?i)(alumn|syllab|vir|radi|nucle|fung|cact|stimul|termin|bacill|foc|uter|loc|strat)(?:us|i)$`), "${1}i"},
	{regexp.MustCompile(`(?i)([^l]ias|[aeiou]las|[ejzr]as|[iu]am)$`), "${1}"},
	{regexp.MustCompile(`(?i)(e[mn]u)s?$`), "${1}s"},
	{regexp.MustCompile(`(?i)(alias|[^aou]us|t[lm]as|gas|ris)$`), "${1}es"},
	{regexp.MustCompile(`(?i)(ax|test)is$`), "${1}es"},
	{regexp.MustCompile(`(?i)([^aeiou]ese)$`), "${1}"},
	{regexp.MustCompile(`(?i)s?$`), "s"},
}

func pluralize(word string) string {
	lower := strings.ToLower(word)
	if uncountableWords[lower] {
		return word
	}
	for _, rule := range uncountableRules {
		if rule.MatchString(word) {
			return word
		}
	}
	if irregular, ok := irregularPlurals[lower]; ok {
		return word[:1] + irregular[1:]
	}
	for _, rule := range pluralRules {
		if location := rule.pattern.FindStringSubmatchIndex(word); location != nil {
			var replaced []byte
			replaced = rule.pattern.ExpandString(replaced, rule.replacement, word, location)
			return word[:location[0]] + string(replaced) + word[location[1]:]
		}
	}
	return word + "s"
}
