#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-/workspace/board-games-saas}"

if [ -e "$TARGET_DIR" ]; then
  echo "Target already exists: $TARGET_DIR"
  exit 1
fi

mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"

git init -b main

cat > README.md <<'MD'
# Board Games SaaS

Multiplayer SaaS platform for:

- Rummikub
- Connect 4
- Snake Co-op (2 players)

## Tech Stack

- Frontend: Next.js + TypeScript
- Backend: NestJS + TypeScript
- Realtime: Socket.IO
- Data: PostgreSQL + Redis

## Monorepo Layout

- `apps/web` - Next.js frontend
- `apps/api` - NestJS backend
- `packages/shared` - shared types/protocols

## Quick Start

```bash
cp .env.example .env
# add env values
```

MD

cat > .gitignore <<'GI'
node_modules
.env
.next
dist
coverage
.DS_Store
*.log
GI

cat > .env.example <<'ENV'
NODE_ENV=development
WEB_PORT=3000
API_PORT=4000
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/boardgames
REDIS_URL=redis://localhost:6379
JWT_SECRET=change-me
ENV

mkdir -p apps/web apps/api packages/shared docs

cat > docs/IMPLEMENTATION_PLAN.md <<'PLAN'
# Implementation Plan

1. Foundation
   - Setup pnpm workspace and turborepo
   - Setup lint, format, CI
2. Auth + Lobby
   - JWT auth, room create/join, presence
3. Connect 4 MVP
4. Snake Co-op MVP
5. Rummikub MVP
6. Billing and hardening
PLAN

cat > docker-compose.yml <<'DC'
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: boardgames
    ports:
      - "5432:5432"
  redis:
    image: redis:7
    ports:
      - "6379:6379"
DC

git add .
git commit -m "chore: initialize board-games-saas repository scaffold"

echo "Created new repository at $TARGET_DIR"
