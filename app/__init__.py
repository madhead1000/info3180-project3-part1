from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zcwkqiaibgqscu:TvKLUwuaDb2FVqmi2VJNiWS4Wm@ec2-23-21-219-209.compute-1.amazonaws.com:5432/dfk7jdccbl88m8''
db = SQLAlchemy(app)

from app import views, models
