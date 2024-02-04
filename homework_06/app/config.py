import datetime
from string import ascii_lowercase
import secrets
import os

class Config(object):
    DEBUG = False
    TESTING = False
    ENV = ""
    SECRET_KEY = ''.join(secrets.choice(i) 
                         for i in [x + ascii_lowercase[int(x)] for x in str(datetime.datetime.now()) if x.isdigit()])
    SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI","postgresql+psycopg2://postgres:password@localhost:5432/postgres")
    SQLALCHEMY_ECHO = False


class Prod(Config):
    ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI","postgresql+psycopg2://postgres:password@pg:5432/postgres")


class Dev(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True


