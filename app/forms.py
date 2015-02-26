gitfrom flask.ext.wtf import Form
from wtforms.fields import TextField, FileField, SelectField, SubmitField, IntegerField
from wtforms.validators import Required
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf.file import file_required, file_allowed


class UploadSet(object):
  def __init__(self, name='files', extensions=None):
    self.name = name
    self.extensions = extensions

  def file_allowed(self, storage, basename):
    if not self.extensions:
      return True

    ext = basename.rsplit('.', 1)[-1]
    return ext in self.extensions

images = UploadSet('images', ['jpg', 'png'])


class ProfileForm(Form):
  pic = FileField("Upload file")
  fname = TextField('First Name', validators=[Required("Please enter your First Name.")])
  lname = TextField('Last Name', validators=[Required("Please enter your Last Name.")])
  sex = SelectField('Sex', choices=[
        ('male','Male'),('female','Female')])
  age = IntegerField('Age', validators=[Required("Please enter your age.")])
  submit = SubmitField('Create Account')
  