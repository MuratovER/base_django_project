# Base django project
![alt text](https://img.shields.io/badge/python-3.11.2-orange)

## Technology stack

1. Django
3. PostgreSQL
4. DRF
5. Docker, docker compose

## Run

#### Run local environment stack
```shell
docker-compose up -d --build
```

#### Install poetry
```shell
pip install poetry
```

#### Install the project dependencies
```shell
cd src && poetry install
```

#### Spawn a shell within the virtual environment
```shell
poetry shell
```

#### Run the server
```shell
python manage.py runserver 0.0.0.0:8000
```

## Migrations
```shell
python manage.py makemigration
```

#### Run migrations
```shell
python manage.py migrate
```

#### Downgrade last migration
```shell
python manage.py migrate my_app {migration_number}

```

## Development

#### Make lint, tests
```shell
cd src && make lint
cd src && make test
```

#### Branch naming
```
feature/{feature-name-in-kebab-case}  # branch with new functionality, code
fix/{fix-name-in-kebab-case}  # branch with fix changes
```

#### Commit messages
```
+ {message}  # adding new functionality, code
- {message}  # removing functionality, code
! {message}  # changing functionality, code
```
