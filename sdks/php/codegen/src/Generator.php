<?php

declare(strict_types=1);

namespace ConjoinCloud\Codegen;

use JsonException;

final class Generator
{
    private const DOCUMENTS = [
        ['openapi.json', 'Api'],
        ['openapi-frontend.json', 'Frontend'],
    ];

    private const MAX_DOCUMENT_BYTES = 67_108_864;

    public function __construct(
        private readonly string $specDirectory,
        private readonly string $generatedDirectory,
    ) {
    }

    public function run(): array
    {
        $summaries = [];

        foreach (self::DOCUMENTS as [$file, $namespaceSuffix]) {
            $summaries[] = $this->generate($file, $namespaceSuffix);
        }

        return $summaries;
    }

    private function generate(string $file, string $namespaceSuffix): string
    {
        $groups = (new SpecReader($this->readDocument($this->specDirectory . '/' . $file)))->groups();
        $outputDirectory = $this->generatedDirectory . '/' . $namespaceSuffix;
        $files = [];
        $operationCount = 0;

        foreach ($groups as $group) {
            if (!$group instanceof ResourceGroup) {
                throw new CodegenException(sprintf('%s produced an entry that is not a resource group', $file));
            }

            $className = $group->className();
            $folded = strtolower($className);

            if (isset($files[$folded])) {
                throw new CodegenException(sprintf('Two resource groups in %s both generate the class %s', $file, $className));
            }

            $files[$folded] = new GeneratedFile($className . '.php', ClassRenderer::render($group, 'ConjoinCloud\\Generated\\' . $namespaceSuffix));
            $operationCount += count($group->operations());
        }

        $this->replaceDirectory($outputDirectory, $files);

        return sprintf('%s: %d operations in %d classes', $file, $operationCount, count($files));
    }

    private function readDocument(string $path): array
    {
        $size = is_file($path) ? filesize($path) : false;

        if ($size === false || $size > self::MAX_DOCUMENT_BYTES) {
            throw new CodegenException(sprintf('%s is missing or larger than 64 MiB', $path));
        }

        $text = file_get_contents($path);

        if ($text === false) {
            throw new CodegenException(sprintf('Cannot read %s', $path));
        }

        try {
            $document = json_decode($text, true, 512, JSON_THROW_ON_ERROR);
        } catch (JsonException $error) {
            throw new CodegenException(sprintf('%s is not valid JSON: %s', $path, $error->getMessage()));
        }

        if (!is_array($document) || !is_array($document['paths'] ?? null)) {
            throw new CodegenException(sprintf('%s has no paths object', $path));
        }

        return $document;
    }

    private function replaceDirectory(string $directory, array $files): void
    {
        if (!is_dir($directory) && !mkdir($directory, 0o775, true) && !is_dir($directory)) {
            throw new CodegenException(sprintf('Cannot create %s', $directory));
        }

        $existing = glob($directory . '/*.php');

        foreach ($existing === false ? [] : $existing as $stale) {
            if (!unlink($stale)) {
                throw new CodegenException(sprintf('Cannot remove %s', $stale));
            }
        }

        foreach ($files as $file) {
            if (!$file instanceof GeneratedFile || file_put_contents($directory . '/' . $file->name, $file->source) === false) {
                throw new CodegenException(sprintf('Cannot write the generated class in %s', $directory));
            }
        }
    }
}
