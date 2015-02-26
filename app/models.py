from . import db
import views
from random import randint
from marshmallow import Schema, fields

class Test(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  
  userid = db.Column(db.Integer, unique=True)
  
  pic = db.Column(db.String(80))

  fname = db.Column(db.String(80))

  lname = db.Column(db.String(80))
  
  age = db.Column(db.Integer)
  
  sex = db.Column(db.String(8))
  
  date_created = db.Column(db.Date())
  
  High_score = db.Column(db.Integer)
  
  TDollars = db.Column(db.Numeric)
  
  

  def __init__(self, pic, fname, lname, age, sex):
    
    self.userid = randint(10000000,99999999)
    
    self.pic = pic
 
    self.fname = fname

    self.lname = lname
    
    self.age = age
    
    self.sex = sex
    
    self.date_created = views.timeinfo()
    

  def __repr__(self):

    return '<User %r>' % self.fname
  
class UserSchema(Schema):
  formatted_name = fields.Method("format_name")


  class Meta:
    fields = ('fname', 'lname', 'userid', 'pic', 'age', 'sex', 'date_created', 'High_score', 'TDollars')
    