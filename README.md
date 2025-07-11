# PGRechner 3.0

PGRechner ("Pflegegrad Rechner") is a Flask application for calculating care level scores. The repository contains a full Docker setup including PostgreSQL and an Nginx reverse proxy.

## Environment variables

Copy `.env.example` to `.env` and adjust if needed. The application uses these variables to connect to the database and secure sessions:

```env
SECRET_KEY=change-me
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=pgrechner_db_test
DB_PORT=5432
DB_NAME=pgrechner
DATABASE_URL=postgresql://postgres:postgres@pgrechner_db_test:5432/pgrechner
```

`docker-compose` automatically loads values from this file.

## Running with Docker Compose

Install Docker and Docker Compose, then build and start the containers using the external main vps
`docker-compose.yml` :

```bash
docker-compose up --build /root/n8n/docker-compose.yml
```

This starts three services:

- **pgrechner_app_test** – the Flask application listening on port `5001`.
- **pgrechner_db_test** – a PostgreSQL database.
- **pgrechner_nginx_test** – a reverse proxy for the Flask app.
The Compose file relies on an external Nginx proxy for domain routing. When the proxy is configured, visit [http://opbrechner.optimum-pflegeberatung.de](http://opbrechner.optimum-pflegeberatung.de) to reach the application.

Open [http://opbrechner.optimum-pflegeberatung.de](opbrechner.optimum-pflegeberatung.de) once the services are running.

## Running with Docker

You can also run the Flask container directly without Compose:

```bash
docker build -t pgrechner .\
docker run --env-file .env -p 5001:5001 pgrechner
```

This approach requires an accessible PostgreSQL instance and optional Nginx setup.

## Demo credentials

Two demo accounts are available:

- `user` / `userpass`
- `admin` / `adminpass`

The admin account grants access to routes such as `/admin`.

## Development notes

- Variables in `.env` override defaults defined in `docker-compose.yml` and `Dockerfile`.
- Rebuild or restart the `pgrechner_app` service after modifying Python code for changes to take effect.
- Dependencies such as `gunicorn` and `psycopg2-binary` are installed from `requirements.txt`.
- Database files persist in the named `pgrechner_db_data_test` volume between container restarts.
- The production VPS is reachable at `194.5.159.108` . Open [http://opbrechner.optimum-pflegeberatung.de](http://opbrechner.optimum-pflegeberatung.de) to access the application.

## Data files

The application stores calculation history in `data/calculations.json`. The file contains a JSON array of past results and is created automatically if missing. An empty array is provided in the repository so new installations start with a valid file.

## VPS-level Docker Compose

When deploying alongside an existing `nginx-proxy`, add the following services to
the VPS `docker-compose.yml`. Each service joins the `proxy_network` so requests
for `opbrechner.optimum-pflegeberatung.de` are routed correctly.

```yaml
services:
  pgrechner_app_test:
    build: ./PGRechner3.0
    container_name: pgrechner_app_test
    env_file: ./PGRechner3.0/.env
    depends_on:
      - pgrechner_db_test
    networks:
      - proxy_network

  pgrechner_db_test:
    image: postgres:15-alpine
    container_name: pgrechner_db_test
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: pgrechner
    volumes:
      - pgrechner_db_data_test:/var/lib/postgresql/data
    networks:
      - proxy_network

  pgrechner_nginx_test:
    image: nginx:alpine
    container_name: pgrechner_nginx_test
    environment:
      - VIRTUAL_HOST=opbrechner.optimum-pflegeberatung.de
      - LETSENCRYPT_HOST=opbrechner.optimum-pflegeberatung.de
      - LETSENCRYPT_EMAIL=alex.torrescanety@optimum-pflegeberatung.de
    volumes:
      - ./PGRechner3.0/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - pgrechner_app_test
    networks:
      - proxy_network

volumes:
  pgrechner_db_data_test:

networks:
  proxy_network:
    external: true
```

This configuration mirrors the Compose setup in the repository while ensuring a
persistent database volume and loading `nginx.conf` from this project.


## Running tests

Unit tests are provided for the core calculator logic. Install dependencies and run the test suite with:

```bash
pytest
```