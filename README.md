# PGRechner 3.0

PGRechner ("Pflegegrad Rechner") is a Flask application for calculating care level scores. The repository contains a full Docker setup including PostgreSQL and an Nginx reverse proxy.

## Environment variables

Create a `.env` file in the project root and define the following variables so the app can connect to the database and secure sessions:

```env
SECRET_KEY=change-me
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DB_NAME=pgrechner
DATABASE_URL=postgresql://postgres:postgres@db:5432/pgrechner
```

`docker-compose` automatically loads values from this file.

## Running with Docker Compose

Install Docker and Docker Compose, then build and start the containers:

```bash
docker-compose up --build
```

This starts three services:

- **app** – the Flask application listening on port `5000`.
- **db** – a PostgreSQL database.
- **nginx** – a reverse proxy exposing the app on port `80`.

Open [http://localhost](http://localhost) once the services are running.

## Running with Docker

You can also run the Flask container directly without Compose:

```bash
docker build -t pgrechner .
docker run --env-file .env -p 5000:5000 pgrechner
```

This approach requires an accessible PostgreSQL instance and optional Nginx setup.

## Demo credentials

Two demo accounts are available:

- `user` / `userpass`
- `admin` / `adminpass`

The admin account grants access to routes such as `/admin`.

## Development notes

- Variables in `.env` override defaults defined in `docker-compose.yml` and `Dockerfile`.
- Rebuild or restart the `app` service after modifying Python code for changes to take effect.
- Database files persist in the named `db-data` volume between container restarts.