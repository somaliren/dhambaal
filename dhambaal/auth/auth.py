from flask import Blueprint, render_template, url_for, flash, redirect
from dhambaal.auth.model import User
from dhambaal.auth.forms import LoginForm, RegisterForm


auth = Blueprint("auth", __name__, template_folder="templates")

# Register Route


@auth.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        # TODO1 : Compare hashed password with users password
        # TODO2. Check if email and password match
        #  User login
        flash("Logged in successfully", 'is-success')
        return redirect(url_for("dashboard.index"))
    return render_template("login.html", form=form)
