import { mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

import { collectResourceGroups } from './operations'
import { moduleFileName, renderBarrel, renderModule } from './render'

const codegenDir = resolve(fileURLToPath(import.meta.url), '..')
const specDir = resolve(codegenDir, '../../../spec')
const generatedDir = resolve(codegenDir, '../src/generated')

type GeneratedDocument = {
  specFile: string
  outputDir: string
  apiTypesImport: string
}

const DOCUMENTS: GeneratedDocument[] = [
  { specFile: 'openapi.json', outputDir: 'modules', apiTypesImport: '../api-types' },
  { specFile: 'openapi-frontend.json', outputDir: 'frontend', apiTypesImport: '../frontend-api-types' },
]

function generate(document: GeneratedDocument): void {
  const spec = JSON.parse(readFileSync(resolve(specDir, document.specFile), 'utf-8'))
  const groups = collectResourceGroups(spec)
  const outputDir = resolve(generatedDir, document.outputDir)

  rmSync(outputDir, { recursive: true, force: true })
  mkdirSync(outputDir, { recursive: true })

  const services = new Set<string>()
  let operationCount = 0

  for (const group of groups) {
    services.add(group.service)
    operationCount += group.operations.length
    writeFileSync(
      resolve(outputDir, `${moduleFileName(group)}.ts`),
      renderModule(group, document.apiTypesImport, '../../core'),
      'utf-8',
    )
  }

  for (const service of services) {
    writeFileSync(resolve(outputDir, `${service}-index.ts`), renderBarrel(groups, service), 'utf-8')
  }

  console.log(`${document.specFile}: ${operationCount} operations in ${groups.length} modules`)
}

for (const document of DOCUMENTS) {
  generate(document)
}
