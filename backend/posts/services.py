from typing import Any

from sqlalchemy import func

from app import db
from models import Post, Tag

from .forms import PostForm


def get_filtered_posts(search_query: str) -> list[Any]:
    if search_query:
        return Post.query.filter(
            func.lower(Post.title).contains(search_query.lower())
            | func.lower(Post.body).contains(search_query.lower())
        )
    else:
        return Post.query.order_by(Post.created.desc())


def get_specific_post(slug: str) -> Post:
    return Post.query.filter(Post.slug == slug).first_or_404()


def get_specific_tag(slug: str) -> Tag:
    return Tag.query.filter(Tag.slug == slug).first_or_404()


def add_post_to_db(post: Post) -> Post:
    try:
        db.session.add(post)
        db.session.commit()
        return post
    except:
        print("failed to send a create-query to the database")


def update_post(form: PostForm) -> None:
    form.populate_obj(form)
    db.session.commit()
