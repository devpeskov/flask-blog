from flask import render_template  # type: ignore

from app import app


@app.route("/")
@app.route("/blog")
def index():
    return "<h1>Hello world!</h1>"


@app.route("/about")
def about():
    name = "Garrison Bergeron"
    return render_template("about.html", name=name)
