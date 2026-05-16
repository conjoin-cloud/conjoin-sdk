import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'node',
    include: ['src/**/*.test.ts', 'src/**/*.test.tsx'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      reportsDirectory: './tests/coverage',
      include: ['src/**/*.ts', 'src/**/*.tsx'],
      exclude: ['src/generated/**', 'src/**/__tests__/**', '**/*.test.ts', '**/*.test.tsx'],
    },
  },
})
