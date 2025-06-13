# PGRechner 3.0

PGRechner ("Pflegegrad Rechner") is a Flask application used to calculate care level scores. The project ships with a PostgreSQL database and an Nginx reverse proxy for local development.

## Prerequisites

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone this repository.
2. Create a `.env` file in the project root to override default environment variables. The most common settings are:

   ```env
   SECRET_KEY=change-me
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=pgrechner
   DATABASE_URL=postgresql://postgres:postgres@db:5432/pgrechner
   ```

   `docker-compose` automatically loads variables from this file.
3. Build and start the stack:

   ```bash
   docker-compose up --build
   ```

This brings up three services: `app` (the Flask app), `db` (PostgreSQL) and `nginx` which proxies port `80` on the host to the Flask app running on port `5000`.

## Usage

Once the containers are running, open [http://localhost](http://localhost) in your browser. The Flask application listens on port 5000 internally and is exposed via Nginx on port 80.

Two demo users are available for testing:

* `user` / `userpass`
* `admin` / `adminpass`

The admin account grants access to additional routes such as `/admin`.

## Development tips

* Any environment variables defined in `.env` will override the defaults found in `docker-compose.yml` and `Dockerfile`.
* Changes to Python files require rebuilding the `app` service or running it directly with `flask` for quick feedback.
* Database files are stored in the `db-data` named volume and persist between container restarts.