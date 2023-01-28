from flask_sqlalchemy.query import Query

from app import db
from models import Post, Tag

from .forms import PostForm


def get_filtered_posts(search_query: str) -> Query:
    if search_query:
        return db.session.query(Post).filter(
            Post.title.ilike(f"%{search_query}%")
            | Post.body.ilike(f"%{search_query}%")
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
    except Exception as e:
        print("<failed to send a create-query to the database:>", e)


def update_post(form: PostForm, post: Post) -> None:
    form.populate_obj(post)
    post.generate_slug()
    db.session.commit()


def create_tags(raw_tags: list[str]) -> list[Tag]:
    tags: list[Tag] = []
    # prepared tags = tags in lower register, without spaces, dublicates
    prepared_tags = set(
        [
            x.replace(" ", "")[:100].lower()
            for x in raw_tags
            if x.replace(" ", "")
        ]
    )
    if prepared_tags:
        for tag_name in prepared_tags:
            tag = _get_or_create(Tag, name=tag_name)
            tags.append(tag)
    return tags


def _get_or_create(ObjectModel: db.Model, **kwargs) -> db.Model:
    object = db.session.query(ObjectModel).filter_by(**kwargs).first()
    if object:
        return object
    else:
        object = ObjectModel(**kwargs)
        try:
            db.session.add(object)
            db.session.commit()
            return object
        except Exception as e:
            print("<failed to send a create-query to the database:>", e)
