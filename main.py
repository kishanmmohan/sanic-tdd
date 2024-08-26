

import sentry_sdk
from sanic import Sanic, response
from sanic_ext import Extend, openapi
from sentry_sdk.integrations.asyncio import AsyncioIntegration
from tortoise import Tortoise

from app.backends.postgres import APPS_MODELS, connect_database


def initialize_orm(func):
    def wrapped(*args, **kwargs):
        Tortoise.init_models(APPS_MODELS, "models")
        app = func(*args, **kwargs)
        connect_database(app)
        return app

    return wrapped

@initialize_orm
def create_app(configs) -> Sanic:
    app = Sanic("products-app", log_config=configs.LOGGING_CONFIG)
    app.config.update(configs)

    Extend(app)

    if app.config.ENVIRONMENT == "production":
        sentry_sdk.init(
            dsn="sentry_dsn",
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for tracing.
            traces_sample_rate=1.0,
            # Set profiles_sample_rate to 1.0 to profile 100%
            # of sampled transactions.
            # We recommend adjusting this value in production.
            profiles_sample_rate=1.0,
            integrations=[AsyncioIntegration()],
        )

    @openapi.tag("Utility")
    @openapi.summary("Uptime Check")
    @app.route('/uptime')
    async def uptime_check(request):
        return response.json(
            {
                "status": "ok",
                "environment":app.config.ENVIRONMENT
            }
        )
    return app
