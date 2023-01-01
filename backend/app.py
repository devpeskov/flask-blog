from flask import Flask  # type: ignore
from flask_sqlalchemy import SQLAlchemy

from config import Configuration
from posts.blueprint import posts

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

app.register_blueprint(posts, url_prefix="/blog")
