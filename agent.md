Agent Configuration for PGRechner3.0

This document defines the AI agent’s operating context, capabilities, guidelines, and workflows for the PGRechner 3.0 repository. It should be placed at the project root as agent.md and used by Codex (or any AI-powered tooling) when generating, fixing, updating, or deploying code.

1. Purpose

Assist developers in writing, refactoring, and debugging code.

Automate common tasks such as adding new features, writing tests, and updating documentation.

Maintain code quality by enforcing style guidelines, PEP8 compliance, and best practices.

Support deployment by guiding Docker builds, Docker Compose usage, and Nginx configuration.

2. Repository Overview

├── config/           # Application configuration and settings
├── data/             # Persistent data (e.g., calculations.json)
├── modules/          # Business logic and utility functions
├── static/           # CSS, JS, images
├── templates/        # Jinja2 HTML templates
├── .gitignore        # Git exclusions
├── agent.md          # This agent configuration file 
├── Dockerfile        # Container build instructions
├── nginx.conf        # Reverse proxy config
├── requirements.txt  # Python dependencies
├── README.md         # Project overview & usage
├── app.py            # Flask application entrypoint

The agent should familiarize itself with these directories and files before suggesting changes.

3. Environment Variables

All sensitive and environment-specific settings must be defined in a .env file at the project root. The agent should reference and preserve these variables:

SECRET_KEY=change-me
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=pgrechner_db
DB_PORT=5432
DB_NAME=pgrechner
DATABASE_URL=postgresql://postgres:postgres@pgrechner_db:5432/pgrechner

Do not hard-code secrets or credentials in code.

4. Development Workflow

Pull latest changes from main.

Install dependencies: pip install -r requirements.txt or via Docker Compose.

Run tests (when present) before committing changes.

Build and run locally with docker-compose up --build.

Lint and format code: follow PEP8 and apply auto-formatters.

Commit with meaningful messages (see Section 7).

Push and open a Pull Request for review.

For Docker-based workflows, prefer the Compose setup to ensure environment parity.

5. Coding Guidelines

Language: Python 3.8+ (Flask framework).

Style: PEP8, use flake8 and black auto-formatting.

Templates: Jinja2 best practices; avoid inline CSS/JS where possible.

Database: Use SQLAlchemy or psycopg2-binary as configured.

Logging: Use Python’s logging module for server logs.

6. Common Tasks & Patterns

Adding a new route:

Define function in app.py or appropriate module.

Add corresponding template in templates/.

Update navigation links if needed.

Business logic: Keep in modules/, not directly in routes.

Static assets: Place under static/, reference via url_for('static', filename=...).

Data persistence: Read/write JSON in data/calculations.json using thread-safe I/O.

7. Commit Message Conventions

feat: a new feature

fix: a bug fix

docs: documentation only changes

style: formatting, missing semi-colons, etc

refactor: code change without feature or bug fix

test: adding or updating tests

chore: build process or auxiliary tools

Example: fix: handle division-by-zero in care-grade calculation

8. Testing & Validation

If tests exist, run them with pytest or unittest.

Validate JSON schema for calculations.json when writing to data/.

For UI changes, verify templates render correctly in the browser.

9. Deployment

Docker: ensure Dockerfile reflects all dependencies.

Docker Compose: use docker-compose.yml for local orchestration of app, db, and nginx.

Nginx: reverse proxy configuration in nginx.conf must match container ports.

Production: never enable debug mode; verify SECRET_KEY and database credentials are secure.

10. Error Handling

Catch exceptions in routes and return user-friendly error pages (templates/404.html, 500.html).

Log stack traces server-side; do not expose internals to users.