from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = 'app/static/img'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tyydjutwfwjeot:HtrmqJzMDuZhiV3EkL24dsxItu@ec2-54-204-2-217.compute-1.amazonaws.com:5432/dfcc64qaq8k2vd'
db = SQLAlchemy(app)

from app import views, models
