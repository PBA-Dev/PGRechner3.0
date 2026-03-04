# Board Games SaaS Plan (moved to separate repository)

This planning work is **not intended to be implemented inside `PGRechner3.0`**.

## New repository location

Use a dedicated repository for the new product:

- Suggested path: `/workspace/board-games-saas`
- Initial bootstrap script: `scripts/create_board_games_repo.sh`
- Phase-1 scaffolding script: `scripts/scaffold_board_games_phase1.sh`

## Step 1: Create the new repository

```bash
bash scripts/create_board_games_repo.sh /workspace/board-games-saas
```

This initializes a standalone git repository with starter files and base folders.

## Step 2: Implement the first `.md` plan steps (start creating files)

```bash
bash scripts/scaffold_board_games_phase1.sh /workspace/board-games-saas
```

This adds:

1. Monorepo root files (`package.json`, `pnpm-workspace.yaml`, `turbo.json`).
2. Base TS config (`tsconfig.base.json`).
3. `apps/web` skeleton (Next.js app router starter files).
4. `apps/api` skeleton (`src/main.ts` with `/health`).
5. `packages/shared` with common types.
6. Updated implementation plan in `docs/IMPLEMENTATION_PLAN.md`.

## Recommended next actions in the new repository

1. Run `pnpm install`.
2. Replace the API starter with NestJS scaffold.
3. Implement auth + lobby + room lifecycle.
4. Ship Connect 4 first as the first full playable vertical slice.
