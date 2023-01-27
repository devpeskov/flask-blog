from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    name = "Peskov Sergey"
    return render_template("about.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
