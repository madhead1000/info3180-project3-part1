from flask.ext.wtf import Form
from werkzeug import secure_filename
from flask_wtf.file import FileField

class PhotoForm(Form):
    photo = FileField('Your photo')