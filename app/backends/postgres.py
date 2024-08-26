import os

from tortoise.contrib.sanic import register_tortoise

APPS_MODELS = [
    "app.services.product.models"
]

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": os.getenv("POSTGRES_DATABASE"),
                "host": os.getenv("POSTGRES_HOST"),
                "password": os.getenv("POSTGRES_PASSWORD"),
                "port": os.getenv("POSTGRES_PORT"),
                "user": os.getenv("POSTGRES_USER"),
            }
        }
    },
    "apps": {
        "models": {
            "models": APPS_MODELS,
            "default_connection": "default",
        },
    },
}


def connect_database(app) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
    )
