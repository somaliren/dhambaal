from flask import Blueprint, render_template, url_for, flash, redirect
from flask.helpers import get_env
from dhambaal.auth.model import User
from dhambaal.auth.forms import LoginForm, RegisterForm
# from werkzeug.security import check_password_hash, generate_password_hash
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from dhambaal.utils.mail import send


auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/login/", methods=['POST', 'GET'])
def login():
    # TODO 1: if user is already logged in we need to redirect to dashboard
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    # select * from users where email = 'test@test.com'

    if form.validate_on_submit():
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in successfully", 'is-success')
            send(recipients="amiin@asalsolutions.com",
                 subject="Test Email", message="This is a test email")
            return redirect(url_for("dashboard.index"))
        else:
            flash("Invalid Credentials", 'is-danger')
            return redirect(url_for("auth.login"))

        # TODO 2 : Compare hashed password with users password
        # TODO 3. Check if email and password match
        #  User login

    return render_template("login.html", form=form)


@auth.route('/dashboard/user/logout')
@login_required
def logout():
    # CHECK IF USER IS LOGGED IN TO LOGOUT
    logout_user()
    flash("Logout successfully", 'is-success')
    return redirect(url_for("auth.login"))

# Register Route


@auth.route("/dashboard/user/register", methods=['POST', 'GET'])
@login_required
def register_user():
    form = RegisterForm()

    if form.validate_on_submit():
        # TODO 2 : check if admin or staff
        # if username or email is already taken display error message
        user = User(name=form.name.data, email=form.email.data,
                    username=form.username.data, password=generate_password_hash(form.password.data).decode("utf-8"))
        user.save()
        flash("User created successfully", 'is-success')
        return redirect(url_for("auth.users"))
    return render_template("register.html", form=form, title="Add User")


@auth.route("/dashboard/users")
@login_required
def users():
    users = User.query.all()
    return render_template("users.html", users=users)

# A = 95
# a = 67


#  128   64  32 16  8  4  2  1
# 0     1     0  0   0  0  0    1
