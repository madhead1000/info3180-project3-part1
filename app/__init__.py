from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'
db = SQLAlchemy(app)

from app import views, models
