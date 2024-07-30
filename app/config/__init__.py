import importlib
import os

from sanic.config import Config

from app.config.environments.development import DevelopmentConfig
from app.config.environments.production import ProductionConfig
from app.config.environments.testing import TestingConfig

config_path = os.getenv("SANIC_CONFIG_MODULE", "app.config.environments.development")
config_module = importlib.import_module(config_path)

config = Config()


def load_config():
    """Load configuration based on environment."""
    env = os.getenv('FLASK_ENV', 'development').lower()

    if env == 'development':
        config_class = DevelopmentConfig
    elif env == 'testing':
        config_class = TestingConfig
    elif env == 'production':
        config_class = ProductionConfig
    else:
        raise ValueError(f"Unknown environment: {env}")

    # Update the app's config with the selected configuration class
    vars = config_class.get_vars()
    return vars


vars = load_config()
config.update_config(vars)
