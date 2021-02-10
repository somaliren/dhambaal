from operator import pos
from flask import render_template, request, redirect
from dhambaal import app
from dhambaal.models.Post import Post


@app.route("/", methods=['GET'])
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


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
