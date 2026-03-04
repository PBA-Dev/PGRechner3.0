#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-/workspace/board-games-saas}"

if [ ! -d "$TARGET_DIR/.git" ]; then
  echo "Expected an initialized git repository at: $TARGET_DIR"
  echo "Tip: run scripts/create_board_games_repo.sh first"
  exit 1
fi

cd "$TARGET_DIR"

mkdir -p apps/web/src/app apps/api/src packages/shared/src

cat > package.json <<'JSON'
{
  "name": "board-games-saas",
  "private": true,
  "packageManager": "pnpm@9.12.1",
  "scripts": {
    "build": "turbo run build",
    "dev": "turbo run dev --parallel",
    "lint": "turbo run lint",
    "test": "turbo run test"
  },
  "devDependencies": {
    "turbo": "^2.1.3",
    "typescript": "^5.6.2"
  }
}
JSON

cat > pnpm-workspace.yaml <<'YAML'
packages:
  - apps/*
  - packages/*
YAML

cat > turbo.json <<'JSON'
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "lint": {},
    "test": {}
  }
}
JSON

cat > tsconfig.base.json <<'JSON'
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "baseUrl": ".",
    "paths": {
      "@bg/shared/*": ["packages/shared/src/*"]
    }
  }
}
JSON

cat > apps/web/package.json <<'JSON'
{
  "name": "@bg/web",
  "private": true,
  "scripts": {
    "dev": "next dev -p 3000",
    "build": "next build",
    "start": "next start -p 3000",
    "lint": "echo 'TODO: add eslint config'",
    "test": "echo 'TODO: add web tests'"
  },
  "dependencies": {
    "next": "14.2.15",
    "react": "18.3.1",
    "react-dom": "18.3.1"
  },
  "devDependencies": {
    "typescript": "^5.6.2"
  }
}
JSON

cat > apps/web/tsconfig.json <<'JSON'
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "jsx": "preserve",
    "allowJs": true,
    "noEmit": true,
    "incremental": true
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
JSON

cat > apps/web/next.config.js <<'JS'
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true
};

module.exports = nextConfig;
JS

cat > apps/web/src/app/layout.tsx <<'TSX'
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
TSX

cat > apps/web/src/app/page.tsx <<'TSX'
export default function HomePage() {
  return (
    <main>
      <h1>Board Games SaaS</h1>
      <p>Initial scaffold complete. Next: auth, lobby, and game rooms.</p>
    </main>
  );
}
TSX

cat > apps/api/package.json <<'JSON'
{
  "name": "@bg/api",
  "private": true,
  "scripts": {
    "dev": "tsx watch src/main.ts",
    "build": "tsc -p tsconfig.json",
    "start": "node dist/main.js",
    "lint": "echo 'TODO: add eslint config'",
    "test": "echo 'TODO: add api tests'"
  },
  "dependencies": {
    "express": "^4.21.0"
  },
  "devDependencies": {
    "tsx": "^4.19.1",
    "typescript": "^5.6.2"
  }
}
JSON

cat > apps/api/tsconfig.json <<'JSON'
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "dist",
    "module": "CommonJS",
    "moduleResolution": "Node"
  },
  "include": ["src/**/*.ts"]
}
JSON

cat > apps/api/src/main.ts <<'TS'
import express from 'express';

const app = express();
const port = Number(process.env.API_PORT ?? 4000);

app.get('/health', (_req, res) => {
  res.json({ ok: true, service: 'api' });
});

app.listen(port, () => {
  console.log(`API listening on :${port}`);
});
TS

cat > packages/shared/package.json <<'JSON'
{
  "name": "@bg/shared",
  "version": "0.0.1",
  "private": true,
  "main": "src/index.ts",
  "types": "src/index.ts",
  "scripts": {
    "build": "echo 'shared is source-only for now'",
    "lint": "echo 'TODO: add shared lint'",
    "test": "echo 'TODO: add shared tests'"
  }
}
JSON

cat > packages/shared/src/index.ts <<'TS'
export type GameType = 'connect4' | 'rummikub' | 'snake-coop';

export interface HealthResponse {
  ok: boolean;
  service: 'api';
}
TS

cat > docs/IMPLEMENTATION_PLAN.md <<'MD'
# Implementation Plan

## Completed now (initial scaffolding)

- Monorepo root setup (`pnpm-workspace.yaml`, `turbo.json`, root `package.json`).
- Base TypeScript config (`tsconfig.base.json`).
- `apps/web` skeleton with Next.js app router files.
- `apps/api` skeleton with a minimal Express health endpoint.
- `packages/shared` for shared types.

## Next steps

1. Install dependencies with `pnpm install`.
2. Replace Express API with NestJS scaffold.
3. Implement JWT auth module.
4. Add lobby and room lifecycle over WebSockets.
5. Deliver Connect 4 first as vertical slice.
MD

if ! git diff --quiet || ! git diff --cached --quiet; then
  git add .
  git commit -m "feat: add phase-1 monorepo scaffolding for board-games-saas"
  echo "Scaffold committed in $TARGET_DIR"
else
  echo "No changes detected in $TARGET_DIR"
fi
