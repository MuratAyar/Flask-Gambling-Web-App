# Flask-Gambling-Web-App

A personal project which includes Docker, Jinja 2 Templates, CLI Scripts, Contact and automated email System, Recurring Payments with Stripe, Flask web applications, Detailed Registration and Login Systems, Admin Panel, Celery, Click, SQLAlchemy and suitable for PostgreSQL admin panel pgAdmin 4.

```shell
git clone https://github.com/MuratAyar/Flask-Gambling-Web-App.git
cd Flask-Gambling-Web-App/
docker-compose up --build
```

## Developing

## Built With
- Python
- Sublime Text 3
- Ubuntu 22.04.3

## Building
This project does not require any additional building steps.
Only an database building is necessary:

```shell
docker-compose exec --user "$(id -u):$(id -g)" website alembic revision -m "create foo table"
```

## Deploying / Publishing
There are no specific deployment steps for this project. It is designed for analysis and exploration purposes.

## Configuration
No user-configurable parameters. The configuration involves installing the required dependencies and setting up the environment.

## API Reference
This project on external APIs. Flask's Strip Extension and G-mail API Password is necessary. You neep to get an Gmail and Strip keys. And edit the file instances/setting.py accordingly.
