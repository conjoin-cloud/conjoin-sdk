<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

final class Pluralizer
{
    private const UNCOUNTABLE = [
        'adulthood', 'advice', 'agenda', 'aid', 'aircraft', 'alcohol', 'ammo', 'analytics', 'anime', 'athletics',
        'audio', 'bison', 'blood', 'bream', 'buffalo', 'butter', 'carp', 'cash', 'chassis', 'chess', 'clothing',
        'cod', 'commerce', 'cooperation', 'corps', 'debris', 'diabetes', 'digestion', 'elk', 'energy', 'equipment',
        'excretion', 'expertise', 'firmware', 'flounder', 'fun', 'gallows', 'garbage', 'graffiti', 'hardware',
        'headquarters', 'health', 'herpes', 'highjinks', 'homework', 'housework', 'information', 'jeans', 'justice',
        'kudos', 'labour', 'literature', 'machinery', 'mackerel', 'mail', 'media', 'mews', 'moose', 'music', 'mud',
        'manga', 'news', 'only', 'personnel', 'pike', 'plankton', 'pliers', 'police', 'pollution', 'premises',
        'rain', 'research', 'rice', 'salmon', 'scissors', 'series', 'sewage', 'shambles', 'shrimp', 'software',
        'staff', 'swine', 'tennis', 'traffic', 'transportation', 'trout', 'tuna', 'wealth', 'welfare', 'whiting',
        'wildebeest', 'wildlife', 'you',
    ];

    private const UNCOUNTABLE_RULES = ['/[^aeiou]ese$/i', '/deer$/i', '/fish$/i', '/measles$/i', '/o[iu]s$/i', '/pox$/i', '/sheep$/i'];

    private const IRREGULARS = [
        'child' => 'children',
        'die' => 'dice',
        'echo' => 'echoes',
        'foot' => 'feet',
        'genus' => 'genera',
        'goose' => 'geese',
        'human' => 'humans',
        'man' => 'men',
        'ox' => 'oxen',
        'person' => 'people',
        'quiz' => 'quizzes',
        'tooth' => 'teeth',
        'woman' => 'women',
    ];

    private const RULES = [
        ['/m[ae]n$/i', 'men'],
        ['/eaux$/i', '$0'],
        ['/(child)(?:ren)?$/i', '$1ren'],
        ['/(pe)(?:rson|ople)$/i', '$1ople'],
        ['/\b((?:tit)?m|l)(?:ice|ouse)$/i', '$1ice'],
        ['/(matr|cod|mur|sil|vert|ind|append)(?:ix|ex)$/i', '$1ices'],
        ['/(x|ch|ss|sh|zz)$/i', '$1es'],
        ['/([^ch][ieo][ln])ey$/i', '$1ies'],
        ['/([^aeiouy]|qu)y$/i', '$1ies'],
        ['/(?:(kni|wi|li)fe|(ar|l|ea|eo|oa|hoo)f)$/i', '$1$2ves'],
        ['/sis$/i', 'ses'],
        ['/(apheli|hyperbat|periheli|asyndet|noumen|phenomen|criteri|organ|prolegomen|hedr|automat)(?:a|on)$/i', '$1a'],
        [
            '/(agend|addend|millenni|dat|extrem|bacteri|desiderat|strat|candelabr|errat|ov|symposi|curricul|automat|quor)(?:a|um)$/i',
            '$1a',
        ],
        ['/(her|at|gr)o$/i', '$1oes'],
        ['/(seraph|cherub)(?:im)?$/i', '$1im'],
        ['/(alumn|alg|vertebr)(?:a|ae)$/i', '$1ae'],
        ['/(alumn|syllab|vir|radi|nucle|fung|cact|stimul|termin|bacill|foc|uter|loc|strat)(?:us|i)$/i', '$1i'],
        ['/([^l]ias|[aeiou]las|[ejzr]as|[iu]am)$/i', '$1'],
        ['/(e[mn]u)s?$/i', '$1s'],
        ['/(alias|[^aou]us|t[lm]as|gas|ris)$/i', '$1es'],
        ['/(ax|test)is$/i', '$1es'],
        ['/([^aeiou]ese)$/i', '$1'],
        ['/s?$/i', 's'],
    ];

    private function __construct()
    {
    }

    public static function pluralize(string $word): string
    {
        $lower = strtolower($word);

        if (in_array($lower, self::UNCOUNTABLE, true)) {
            return $word;
        }

        foreach (self::UNCOUNTABLE_RULES as $rule) {
            if (preg_match($rule, $word) === 1) {
                return $word;
            }
        }

        $irregular = self::IRREGULARS[$lower] ?? null;

        if ($irregular !== null) {
            return substr($word, 0, 1) . substr($irregular, 1);
        }

        foreach (self::RULES as [$rule, $replacement]) {
            if (preg_match($rule, $word) === 1) {
                return (string) preg_replace($rule, $replacement, $word, 1);
            }
        }

        return $word . 's';
    }
}
