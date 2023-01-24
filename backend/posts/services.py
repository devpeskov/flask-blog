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


def update_post(form: PostForm) -> None:
    form.populate_obj(form)
    db.session.commit()


def create_tags(tag_line: str) -> list[Tag]:
    tags: list[Tag] = []
    if tag_line:
        tags_list = tag_line.replace(" ", "").split(",")
        for tag_name in tags_list:
            tag = _get_or_create(Tag, name=tag_name[:100])
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
        except:
            print("failed to send a create-query to the database")
