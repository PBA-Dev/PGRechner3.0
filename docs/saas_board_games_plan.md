# Board Games SaaS Plan (moved to separate repository)

This planning work is **not intended to be implemented inside `PGRechner3.0`**.

## New repository location

Use a dedicated repository for the new product:

- Suggested path: `/workspace/board-games-saas`
- Bootstrap script in this repo: `scripts/create_board_games_repo.sh`

## How to create the new repository

```bash
bash scripts/create_board_games_repo.sh /workspace/board-games-saas
```

The script will:

1. Create and initialize a new standalone git repository.
2. Add starter files (`README.md`, `.env.example`, `.gitignore`).
3. Add baseline folders (`apps/web`, `apps/api`, `packages/shared`, `docs`).
4. Add a minimal `docker-compose.yml` with Postgres + Redis.
5. Make an initial commit in the **new repository**.

## Recommended next actions in the new repository

1. Initialize `pnpm` workspace + Turborepo.
2. Scaffold `Next.js` app in `apps/web`.
3. Scaffold `NestJS` app in `apps/api`.
4. Implement auth + lobby + room lifecycle.
5. Deliver Connect 4 as the first end-to-end vertical slice.
