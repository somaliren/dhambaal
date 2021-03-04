from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

from wtforms.validators import DataRequired, length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[
                        DataRequired(), length(min=3, max=20)])
    description = TextAreaField("Description", validators=[
                                DataRequired(), length(min=3, max=1500)])
    source = StringField('Source', validators=[
        DataRequired(), length(min=3, max=20)])
    submit = SubmitField('Create')
