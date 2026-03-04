# SaaS Board Games Platform Plan

## 1) Product Scope and Goals

Build a multiplayer SaaS web platform where authenticated users can create/join game sessions and play:

- **Rummikub** (turn-based tile game).
- **Connect 4** (turn-based board game).
- **Snake Co-op 2P** (real-time cooperative snake with collision constraints between snakes).

Primary outcomes:

1. Reliable real-time gameplay.
2. Secure account system and session management.
3. Deployable on a **Hostinger VPS (Ubuntu)**.
4. Foundation for subscription billing and future game additions.

---

## 2) Recommended Tech Stack ("best language" choice)

### Why TypeScript for this project

For multiplayer browser games with authentication, websockets, and maintainability, **TypeScript** provides the best practical balance:

- Shared typings between front-end and back-end reduce protocol bugs.
- Excellent ecosystem for WebSocket/game-room architecture.
- Strong tooling for scaling features, testability, and onboarding.
- Easy deployment on Ubuntu VPS with Docker.

### Stack decision

- **Frontend**: Next.js (React + TypeScript), Tailwind CSS, Zustand or Redux Toolkit.
- **Backend API**: NestJS (TypeScript), REST + WebSocket gateways.
- **Realtime layer**: Socket.IO (or Colyseus if we want built-in room/state patterns).
- **Database**: PostgreSQL.
- **Cache/pub-sub**: Redis (room presence, events, and scale-out support).
- **ORM**: Prisma.
- **Auth**: JWT with refresh token rotation + email verification.
- **Background jobs**: BullMQ (optional in phase 2) for emails, cleanup, analytics batching.
- **Infra**: Docker Compose (dev), Docker + Nginx + systemd (prod).
- **Observability**: Pino logs, Prometheus metrics endpoint, optional Grafana.

Alternative considered: Python (FastAPI + websockets) could work, but TypeScript has stronger web-game ecosystem and better shared-type ergonomics for this use case.

---

## 3) High-Level Architecture

1. **Web client (Next.js)**
   - Handles auth UI, lobby, game rooms, and responsive board rendering.
   - Maintains local optimistic state; reconciles with server-authoritative events.

2. **API + Realtime server (NestJS)**
   - REST for auth, profile, billing, static game metadata.
   - WebSocket namespaces for lobby and per-game sessions.
   - Server-authoritative game engines (never trust client moves).

3. **PostgreSQL**
   - Users, sessions, subscriptions, game history, leaderboards, audit logs.

4. **Redis**
   - Socket presence, distributed room state metadata, pub/sub for multi-instance websocket scale.

5. **Nginx reverse proxy**
   - TLS termination, websocket upgrade routing, static caching.

---

## 4) Core Functional Requirements

### Accounts & Access

- Sign up, login, logout.
- Email verification.
- Password reset.
- User profile and avatar.
- Optional OAuth (Google) in later phase.

### Lobby and Matchmaking

- Public lobby listing open rooms by game.
- Private room codes for friend invites.
- Room owner controls: start game, kick, set options.
- Presence indicators (online, in room, in game).

### Game requirements

#### A) Connect 4

- 2 players.
- Turn validation server-side.
- Win/draw detection on each move.
- Reconnect support and state sync.
- Match history storage.

#### B) Rummikub (initial online version)

- 2-4 players.
- Tile bag generation/shuffling server-side.
- Rack visibility only to owner.
- Table meld validation (runs/groups, jokers).
- Turn timer + draw/pass logic.
- Round completion and scoring.

> Note: Rummikub rules have variants. We should lock one canonical ruleset (e.g., Sabra-like baseline) in an RFC before coding.

#### C) Snake Co-op 2P

- Real-time tick loop (e.g., 8-12 ticks/sec).
- Two snakes on shared board.
- Collision rules:
  - Snake cannot hit walls.
  - Snake cannot hit self.
  - Snake cannot hit other snake body/head per selected mode.
- Shared objective score.
- Optional powerups in phase 2.

### Security & Compliance

- Rate limiting and anti-bruteforce login protection.
- Input validation (DTO schemas everywhere).
- CSRF protections where applicable.
- Secure cookies and token rotation.
- Basic GDPR-ready data deletion endpoint.

---

## 5) Non-Functional Requirements

- **Performance**: P95 move-ack under 150ms (regional deployment).
- **Availability**: graceful reconnect logic; room state recovery.
- **Scalability**: horizontal websocket nodes via Redis adapter.
- **Maintainability**: clean modular game engine boundaries.
- **Testability**: deterministic game-engine unit tests.

---

## 6) Data Model (initial)

- `users`
- `auth_sessions`
- `refresh_tokens`
- `rooms`
- `room_participants`
- `games`
- `game_events` (append-only log)
- `game_snapshots` (periodic state snapshots)
- `subscriptions` (for SaaS billing later)

Design principle:
- Keep game state authoritative in memory for active rooms.
- Persist event log + snapshots for replay/recovery and anti-cheat auditing.

---

## 7) Realtime Protocol Design

Use explicit event contracts with versioning:

- Client -> server: `room.create`, `room.join`, `game.action`, `game.ready`, `game.leave`.
- Server -> client: `room.state`, `game.state`, `game.event`, `game.error`, `game.over`.

Rules:

- Validate every payload with schema (Zod/class-validator).
- Idempotency keys for critical commands.
- Include `serverTime` + `stateVersion` in authoritative messages.

---

## 8) Game Engine Strategy

Each game has a pure deterministic engine package:

- Input: previous state + action.
- Output: next state + emitted events + validity status.

Structure:

- `packages/game-engine-connect4`
- `packages/game-engine-rummikub`
- `packages/game-engine-snake-coop`

Benefits:

- High unit-test coverage.
- Potential future reuse for AI bots/spectators/replays.
- Safer refactors with snapshot tests.

---

## 9) UX Plan

Pages:

1. Landing/pricing.
2. Auth pages.
3. Dashboard/lobby.
4. Room page (chat + players + ready states).
5. Game views:
   - Connect 4 board UI.
   - Rummikub rack/table UI.
   - Snake canvas UI.
6. Profile/settings.

UX essentials:

- Fast reconnect prompts.
- Clear turn indicators and timers.
- Action history panel (especially for Rummikub).
- Accessibility (keyboard interactions and contrast).

---

## 10) Delivery Phases (Implementation Roadmap)

### Phase 0 — Discovery and Rules Finalization (3-5 days)

- Finalize game rule documents (especially Rummikub variants + Snake collision mode).
- Write event contracts and API specs.
- Define MVP vs post-MVP scope.

### Phase 1 — Platform Foundation (1-2 weeks)

- Monorepo setup (pnpm/turborepo).
- Auth system and user management.
- Lobby + room service with websocket infrastructure.
- CI/CD baseline + test scaffolding.

### Phase 2 — Connect 4 MVP (1 week)

- Engine, websocket integration, UI board.
- Reconnect and match history.
- Unit + integration tests.

### Phase 3 — Snake Co-op MVP (1-2 weeks)

- Real-time engine tick loop.
- Two-player synchronized controls.
- Collision/score logic and session lifecycle.

### Phase 4 — Rummikub MVP (2-4 weeks)

- Tile system, meld validation, turn flow.
- Rack privacy handling + complex move rollback validation.
- Scoring and end conditions.

### Phase 5 — SaaS and Production Hardening (1-2 weeks)

- Subscription plans (Stripe) and usage limits.
- Monitoring, backups, security hardening.
- Load tests and optimization.

---

## 11) Testing Strategy

- **Unit tests**: game engines and validators.
- **Integration tests**: websocket flows and room lifecycle.
- **E2E tests**: auth -> lobby -> game complete flow (Playwright).
- **Load tests**: k6 for websocket concurrency and latency.
- **Security tests**: auth abuse, malformed payload fuzzing.

Exit criteria per game:

- Deterministic engine tests >95% pass stability.
- Reconnect success verified.
- At least one full game flow E2E automated.

---

## 12) Deployment Plan (Hostinger VPS Ubuntu)

1. Provision VPS with Docker, Docker Compose plugin, Nginx, Certbot.
2. Run app stack via Compose:
   - `web` (Next.js)
   - `api` (NestJS)
   - `postgres`
   - `redis`
3. Nginx routes:
   - `/` -> web
   - `/api` + websocket upgrades -> api
4. Enable TLS via Let’s Encrypt.
5. Setup systemd service for Compose auto-restart.
6. Configure automated nightly DB backups + offsite sync.
7. Set up CI deploy pipeline (GitHub Actions) to VPS over SSH.

---

## 13) Security Checklist

- Enforce HTTPS and secure cookies.
- Hash passwords with Argon2.
- JWT short-lived access tokens + rotating refresh tokens.
- IP-based and account-based rate limits.
- Server-side authorization checks on every room/game action.
- Secrets in environment variables only.
- Dependency vulnerability scanning in CI.

---

## 14) Risks and Mitigations

1. **Rummikub complexity** -> mitigate with strict rules RFC + incremental validator implementation.
2. **Realtime sync bugs** -> authoritative server state + versioned events.
3. **Websocket scaling** -> Redis adapter from day one.
4. **Cheating/client tampering** -> server-only game logic and validation.

---

## 15) Immediate Next Steps (What to build first)

1. Confirm this stack and game rule assumptions.
2. Create architecture decision record (ADR-001) for TypeScript + NestJS + Next.js.
3. Scaffold monorepo and baseline services.
4. Implement auth + lobby + room lifecycle.
5. Ship Connect 4 first as vertical slice.

This sequence gives the fastest path to a usable multiplayer MVP while reducing architectural risk before implementing more complex game logic (Rummikub and Snake co-op).
