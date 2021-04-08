from enum import unique
from dhambaal import db, app, login_manager
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import JSONWebSignatureSerializer as Serializer

# Load User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(244), unique=True, nullable=False)
    # role = db.Column(db.String(40), unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(244), nullable=False)
    confirmed_at = db.Column(db.DateTime())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def validate_email(cls, email):
        email = User.query.filter_by(email=email).first()
        if email:
            return True

    @classmethod
    def valiate_username(cls, username):
        username = User.query.filter_by(username=username).first()
        if username:
            return True

    s = Serializer(app.config['SECRET_KEY'])

    def get_reset_token(self):
        """
        This method gets creates reset token with userId
        examples: 
        user = User.query.filter_by(email=form.email.data)
        token = user.get_reset_token()
         """
        return self.s.dumps({"user_id": self.id}).decode("utf-8")

    @classmethod
    def verify_reset_token(cls, token):
        try:
            user_id = cls.s.loads(token).get('user_id')
        except:
            return None
        return User.query.get(user_id)
