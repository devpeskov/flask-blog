import random
import re
import string
from datetime import datetime

from flask_security import RoleMixin, UserMixin

from app import db

post_tags = db.Table(
    "post_tags",
    db.Column(
        "post_id",
        db.ForeignKey("post.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    db.Column(
        "tag_id",
        db.ForeignKey("tag.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.title = self.title[:140]
        self.generate_slug()

    tags = db.relationship(
        "Tag", secondary=post_tags, backref=db.backref("posts", lazy="dynamic")
    )

    def generate_slug(self):
        if self.title:
            self.slug = _slugify(Post, self.title.lower()[:70])

    def __repr__(self):
        return f"<post id: {self.id}, title: {self.title}>"


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    slug = db.Column(db.String(100), unique=True)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.name = self.name[:100].replace(" ", "").lower()
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = _slugify(Tag, self.name[:70])

    def __repr__(self):
        return self.name


roles_users = db.Table(
    "roles_users",
    db.Column(
        "user_id",
        db.ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    db.Column(
        "role_id",
        db.ForeignKey("role.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        "Role",
        secondary=roles_users,
        backref=db.backref("users", lazy="dynamic"),
    )


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))


def _slugify(ObjectModel: db.Model, string: str) -> str:
    pattern = r"[^\w+]"
    slug = re.sub(pattern, "-", string)

    is_object_exists = db.session.query(
        db.exists().where(ObjectModel.slug == slug)
    ).scalar()

    if is_object_exists:
        new_unique_slug = f"{slug}-{_random_string_generator(size=5)}"

        # Additional recursive-check if the new_unique_slug exists too
        if new_unique_slug != _slugify(ObjectModel, new_unique_slug):
            return _slugify(ObjectModel, slug)
        return new_unique_slug
    else:
        return slug


def _random_string_generator(size=10):
    chars = string.ascii_lowercase + string.digits
    random_string = ""
    for i in range(size):
        random_string += random.choice(chars)
    return random_string
