from flask import Flask  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
