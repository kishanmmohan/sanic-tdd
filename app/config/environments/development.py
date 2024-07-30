from .base import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENVIRONMENT = 'development'
