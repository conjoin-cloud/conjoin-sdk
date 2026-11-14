<?php

declare(strict_types=1);

namespace ConjoinCloud\Pagination;

interface PageFetcher
{
    public function fetch(string $nextCursor, array $seenCursors): ListPage;
}
