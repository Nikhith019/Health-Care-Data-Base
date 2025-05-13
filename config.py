import os

class Config:
    """Base configuration with defaults."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/meditrack_db'


class TestingConfig(Config):
    """Configuration used for running tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # Or use 'sqlite:///:memory:' for in-memory testing
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/meditrack_db')
    DEBUG = False
