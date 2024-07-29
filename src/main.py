from routes import blueprint
from sanic import Sanic


def create_app():
    app = Sanic('products-api')
    app.blueprint(blueprint)
    return app


application = create_app()

if __name__ == "__main__":
    application.run(debug=True, access_log=True)
