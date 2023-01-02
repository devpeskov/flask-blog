class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://postgres:@localhost:5432/flask_blog"
    )
