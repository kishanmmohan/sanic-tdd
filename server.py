from app.config import config
from main import create_app

print(config["DEBUG"])

app = create_app(config)

if __name__ == "__main__":
    app.run(
        host=config["HOST"],
        port=config["PORT"],
        debug=config["DEBUG"],
        dev=config["DEBUG"],
        workers=config["WORKERS_COUNT"],
    )
