import view
from app import app, db
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix="/blog")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
