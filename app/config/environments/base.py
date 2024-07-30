import inspect
import os


class BaseConfig:
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    HOST = "0.0.0.0"
    PORT = 8000
    WORKERS_COUNT = 4

    @classmethod
    def get_vars(cls):
        attrs = {}
        # Get all classes in the method resolution order
        for base_cls in inspect.getmro(cls):
            # Update combined dict with attributes from the base_cls
            for key, value in vars(base_cls).items():
                if not key.startswith('__') and key not in attrs:
                    attrs[key] = value
        return attrs
