from flask import render_template  # type: ignore

from app import app


@app.route("/")
@app.route("/blog")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    name = "Peskov Sergey"
    return render_template("about.html", name=name)
