import os

from .base import BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG = False
    SENTRY_DSN = os.environ.get('SENTRY_DSN')
    ENVIRONMENT = 'production'
