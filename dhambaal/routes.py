from operator import pos
from flask import render_template, request, redirect
from dhambaal import app
from dhambaal.models.Post import Post
from dhambaal.models.Categories import Category


@app.route("/", methods=['GET'])
def index():
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template("index.html", posts=posts, categories=categories)


@app.route("/admin", methods=['GET', 'POST'])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        source = request.form.get("source")
        # Inserting form values to the database
        post1 = Post(title=title, description=description, source=source)
        post1.save_to_db()
        return redirect("/")

    return render_template("post_form.html")


@app.route("/category", methods=['GET', 'POST'])
def create_category():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")

        # Inserting form values to the database
        category = Category(name=name, description=description)
        category.save_to_db()
        return redirect("/")

    return render_template("category_form.html")
