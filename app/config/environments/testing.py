from .base import BaseConfig


class TestingConfig(BaseConfig):
    TESTING = True
    ENVIRONMENT = 'testing'
