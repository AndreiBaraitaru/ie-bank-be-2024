from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///local.db'
    DEBUG = True

class GithubCIConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    DEBUG = True

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.getenv('DBUSER'),
    dbpass=os.getenv('DBPASS'),
    dbhost=os.getenv('DBHOST'),
    dbname=os.getenv('DBNAME')
    )
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
        dbuser=os.getenv('PROD_DBUSER'),
        dbpass=os.getenv('PROD_DBPASS'),
        dbhost=os.getenv('PROD_DBHOST'),
        dbname=os.getenv('PROD_DBNAME')
    )
    DEBUG = False

#comments