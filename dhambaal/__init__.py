from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisverysuecure'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dhambaal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Create Tables before running application
@app.before_first_request
def create_tables():
    db.create_all()


# REGISTER BLUEPRINTS
from dhambaal.dashboard.views import dashboard
from dhambaal.views import site
app.register_blueprint(dashboard)
app.register_blueprint(site)
