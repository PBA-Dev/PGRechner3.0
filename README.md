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
- **nginx** – a reverse proxy for the Flask app.
The Compose file relies on an external Nginx proxy for domain routing. When the proxy is configured, visit [http://opbrechner.optimum-pflegeberatung.de](http://opbrechner.optimum-pflegeberatung.de) to reach the application.

Open [http://opbrechner.optimum-pflegeberatung.de](opbrechner.optimum-pflegeberatung.de) once the services are running.

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
- Dependencies such as `gunicorn` and `psycopg2-binary` are installed from `requirements.txt`.
- Database files persist in the named `db-data` volume between container restarts.
- The production VPS is reachable at `194.5.159.108` . Open [http://opbrechner.optimum-pflegeberatung.de](http://opbrechner.optimum-pflegeberatung.de) to access the application.

## Data files

The application stores calculation history in `data/calculations.json`. The file contains a JSON array of past results and is created automatically if missing. An empty array is provided in the repository so new installations start with a valid file.

## VPS-level Docker Compose

When deploying alongside an existing `nginx-proxy`, add the following services to
the VPS `docker-compose.yml`. Each service joins the `proxy_network` so requests
for `opbrechner.optimum-pflegeberatung.de` are routed correctly.

```yaml
services:
  pgrechner_app:
    build: ./PGRechner3.0
    container_name: pgrechner_app
    env_file: ./PGRechner3.0/.env
    depends_on:
      - pgrechner_db
    networks:
      - proxy_network

  pgrechner_db:
    image: postgres:15-alpine
    container_name: pgrechner_db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: pgrechner
    volumes:
      - pgrechner_db_data:/var/lib/postgresql/data
    networks:
      - proxy_network

  pgrechner_nginx:
    image: nginx:alpine
    container_name: pgrechner_nginx
    environment:
      - VIRTUAL_HOST=opbrechner.optimum-pflegeberatung.de
      - LETSENCRYPT_HOST=opbrechner.optimum-pflegeberatung.de
      - LETSENCRYPT_EMAIL=alex.torrescanety@optimum-pflegeberatung.de
    volumes:
      - ./PGRechner3.0/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - pgrechner_app
    networks:
      - proxy_network

volumes:
  pgrechner_db_data:

networks:
  proxy_network:
    external: true
```

This configuration mirrors the Compose setup in the repository while ensuring a
persistent database volume and loading `nginx.conf` from this project.
