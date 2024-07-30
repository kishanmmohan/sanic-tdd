from sanic import Sanic, response
from sanic_ext import Extend


def create_app() -> Sanic:
    app = Sanic("products-app")
    Extend(app)

    @app.route('/health')
    async def health_check(request):
        return response.json({"status": "ok"})

    return app
