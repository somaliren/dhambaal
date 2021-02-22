from flask import Blueprint, render_template

site = Blueprint("site", __name__, url_prefix="/")


@site.route("/")
def index():
    return "Index Page"
