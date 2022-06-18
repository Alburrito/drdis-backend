"""Fichero de configuracion para los distintos entornos de la aplicación"""

from os import environ

class Config(object):
    """Base configuration for the app"""
    FLASK_DEBUG = environ.get('FLASK_DEBUG', 'False')
    FLASK_ENV = environ.get('FLASK_ENV', 'development')
    FLASK_RUN_HOST = environ.get('FLASK_RUN_HOST', '0.0.0.0')
    FLASK_RUN_PORT = environ.get('FLASK_RUN_PORT', '5000')

    CSRF_ENABLED = True
    SECRET_KEY = 'esto-se-tendra-que-cambiar'

    DB_HOST = environ.get('DB_HOST', 'localhost')
    DB_PORT = environ.get('DB_PORT', 27017)
    DB_NAME = environ.get('DB_NAME', 'bug_reports_db')
    DB_USER = environ.get('DB_USER', 'root')
    DB_PASS = environ.get('DB_PASS', 'pass')


class LocalConfig(Config):
    """Configuración para el entorno local.
    Receives variables from .env"""
    FLASK_DEBUG = True

class TestingConfig(Config):
    """Configuration for the test environment.
    Receives variables from .env"""
    FLASK_DEBUG = True
    FLASK_TESTING = True

class StagingConfig(Config):
    """Configuration for the Staging environment.
    Receives variables from staging environment"""
    FLASK_DEBUG = True

class ProductionConfig(Config):
    """Configuration for the production environment.
    Receives variables from production environment"""
    FLASK_DEBUG = False
    FLASK_TESTING = False
