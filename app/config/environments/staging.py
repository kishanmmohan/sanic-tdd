import os

from .base import BaseConfig


class StagingConfig(BaseConfig):
    DEBUG = False
    SENTRY_DSN = os.environ.get('SENTRY_DSN')
    ENVIRONMENT = 'staging'
