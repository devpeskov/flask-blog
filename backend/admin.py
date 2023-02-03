from flask import redirect, request, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, SQLAlchemyUserDatastore, current_user

from app import app, db
from models import Post, Role, Tag, User

# --- Flask-Security ---
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


class SecurityMixin:
    def is_accessible(self):
        return current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("security.login", next=request.url))


class SecuredAdminIndexView(SecurityMixin, AdminIndexView):
    pass


class SecuredModelView(SecurityMixin, ModelView):
    pass


class BaseSlugModelView(SecuredModelView):
    def on_model_change(self, form, model_object, is_created):
        model_object.generate_slug()
        return super().on_model_change(
            form, model_object, is_created
        )


class PostView(BaseSlugModelView):
    form_columns = ["title", "body", "tags"]


class TagView(BaseSlugModelView):
    form_columns = ["name", "posts"]


admin = Admin(
    app,
    name="FlaskApp",
    index_view=SecuredAdminIndexView(name="Home"),
    template_mode="bootstrap4",
)
admin.add_view(PostView(Post, db.session))
admin.add_view(SecuredModelView(User, db.session))
admin.add_view(TagView(Tag, db.session))
admin.add_view(SecuredModelView(Role, db.session))
