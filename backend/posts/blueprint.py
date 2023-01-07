from flask import Blueprint  # type: ignore
from flask import redirect, render_template, request, url_for
from flask_security import login_required  # type: ignore

from models import Post

from .forms import PostForm
from .services import (
    add_post_to_db,
    get_filtered_posts,
    get_specific_post,
    get_specific_tag,
    update_post,
)

posts = Blueprint("posts", __name__, template_folder="templates")


@posts.route("/create", methods=["POST", "GET"])
@login_required
def create_post():
    if request.method == "POST":
        post = add_post_to_db(
            Post(
                title=request.form["title"],
                body=request.form["body"],
            )
        )
        return redirect(url_for("posts.post_detail", slug=post.slug))
    else:
        form = PostForm()
        return render_template("posts/create_post.html", form=form)


@posts.route("/<slug>/edit", methods=["POST", "GET"])
@login_required
def edit_post(slug):
    post = get_specific_post(slug)

    if request.method == "POST":
        update_post(PostForm(formdata=request.form, obj=post))
        return redirect(url_for("posts.post_detail", slug=post.slug))
    else:
        form = PostForm(obj=post)
        return render_template("posts/edit_post.html", post=post, form=form)


@posts.route("/")
def index():
    search_query = request.args.get("q")
    posts = get_filtered_posts(search_query)
    pages = posts.paginate(page=_get_page(), per_page=5)

    return render_template(
        "posts/index.html",
        pages=pages,
        url_for_pagination=_get_url_for_pagination(search_query),
    )


@posts.route("/<slug>")
def post_detail(slug):
    post = get_specific_post(slug)
    tags = post.tags
    return render_template("posts/post_detail.html", post=post, tags=tags)


@posts.route("/tag/<slug>")
def tag_detail(slug):
    tag = get_specific_tag(slug)
    pages = tag.posts.paginate(page=_get_page(), per_page=5)
    return render_template("posts/tag_detail.html", tag=tag, pages=pages)


def _get_page() -> int:
    page = request.args.get("page")

    if page and page.isdigit():
        return int(page)
    else:
        return 1


def _get_url_for_pagination(search_query: str) -> str:
    if search_query:
        return f"./?q={search_query}&page="
    else:
        return "./?page="
