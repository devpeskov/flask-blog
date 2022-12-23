from flask import Flask  # type: ignore

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
