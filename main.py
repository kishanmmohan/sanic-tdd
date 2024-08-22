
import sentry_sdk
from sanic import Sanic, response
from sanic_ext import Extend
from sentry_sdk.integrations.asyncio import AsyncioIntegration


def create_app(configs) -> Sanic:
    app = Sanic("products-app", log_config=configs.LOGGING_CONFIG)
    app.config.update(configs)
    Extend(app)

    if app.config.ENVIRONMENT != "development":
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

    @app.route('/health')
    async def health_check(request):
        return response.json({"status": "ok", "environment":app.config.ENVIRONMENT})

    return app
