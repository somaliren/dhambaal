from flask import Blueprint, render_template
from dhambaal.dashboard.models.Post import Post
from dhambaal.dashboard.models.Categories import Category

admin = Blueprint("admin", __name__,
                  url_prefix="/admin", template_folder="templates")


@admin.route("/")
def index():
    return render_template("dashboard.tmpl")


@admin.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template("posts/posts.tmpl", posts=posts)


@admin.route("/create-post")
def create_post():

    return render_template("posts/create_post.tmpl", posts=posts)


@admin.route("/categories")
def categories():
    categories = Category.query.all()
    return render_template("categories/categories.tmpl", categories=categories)


@admin.route("/create-category")
def create_category():

    return render_template("categories/create_category.tmpl")
