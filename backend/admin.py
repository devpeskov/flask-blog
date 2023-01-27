from flask import redirect, request, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, SQLAlchemyUserDatastore, current_user

from app import app, db
from models import Post, Role, Tag, User


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("security.login", next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(
            form, model, is_created
        )


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ["title", "body", "tags"]


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ["name", "posts"]


admin = Admin(
    app,
    name="FlaskApp",
    index_view=HomeAdminView(name="Home"),
    template_mode="bootstrap4",
)

admin.add_view(PostAdminView(Post, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(AdminView(Role, db.session))

# --- Flask-Security ---
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
