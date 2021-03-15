from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField, PasswordField

from wtforms.validators import DataRequired, Length, Email, EqualTo
# from dhambaal.dashboard.models.Categories import Category


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), Length(min=3)])
    username = StringField('Username', validators=[
        DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[
                        DataRequired(), Email()])
    # TODO 1. Create strong password validation in production
    password = PasswordField("Password", validators=[
        DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(), EqualTo('password', message="Confirm Password field must be equal to password")])
    submit = SubmitField('Create')

    # TODO 1 : Check if username already exist
    # TODO e : Check if email already exist


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email()])
    password = PasswordField("Password", validators=[
        DataRequired()])
    submit = SubmitField('Login')
