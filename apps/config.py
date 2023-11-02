from pathlib import Path
import os

basedir = Path(__file__).parent.parent


class BaseConfig:
    SECRET_KEY = os.environ['SECRET_KEY']
    WTF_CSRF_SECRET_KEY = os.environ['WTF_CSRF_SECRET_KEY']

class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite///{basedir / 'stg.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite///{basedir / 'prd.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

config = {
    'testing': TestingConfig,
    'local': LocalConfig,
    'stg': StagingConfig,
    'prd': ProductionConfig,
}
