from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = 'app/static/img'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uwbpcwnqvigius:RnQlgjf36MMWfv40RdVnt5Mk0S@ec2-50-17-202-29.compute-1.amazonaws.com:5432/d6rkou0c554js0'
db = SQLAlchemy(app)

from app import views, models
