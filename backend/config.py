from os import getenv
from os.path import dirname, join

from dotenv import load_dotenv  # type: ignore

load_dotenv(join(dirname(__file__), "../.env"))


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = getenv("FLASK_SECRET_KEY")
