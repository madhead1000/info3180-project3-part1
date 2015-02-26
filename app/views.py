"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import  time
from app import app
from flask import render_template, request, redirect, url_for
from app import db
from app.models import Test
from .forms import ProfileForm
from flask import jsonify,session,json
from random import randint
from app.models import UserSchema
from werkzeug import secure_filename
from flask_wtf.file import FileField


ALLOWED_EXTENSIONS = set(['png', 'jpg'])

###
# Routing for your application.
###

@app.route('/profile/', methods=["GET", "POST"])
def theform():
  form = ProfileForm(request.form)
  if request.method == 'POST':
    file = request.files['pic']
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      img = filename
      new_user = Test(
        img,
        form.fname.data,
        form.lname.data,
        form.age.data,
        form.sex.data
      )
      db.session.add(new_user)
      db.session.commit()
      return redirect(url_for('theform',
                                    filename=filename))
  return render_template('theform.html',form=form)


def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def timeinfo():
  now = time.strftime("%Y-%m-%d")
  return now

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

  
@app.route('/profiles/', methods=["GET", "POST"])
def get_current_user():
  users = db.session.query(Test).all()
  if request.method =='Post':
    jsonifier = UserSchema(many=True)
    result = jsonifier.dump(users)
    return jsonify({"Users": result.data})
  return render_template('profile.html', users=users)

  
@app.route('/profile/<userid>', methods=["GET", "POST"])
def get_user(userid):
  user= Test.query.filter_by(userid = userid).first()
  if request.method == "GET":
    return render_template('user.html', user=user)
  date=str(user.date_created)
  return jsonify(userid=user.userid, pic=pic, age=user.age, sex=user.sex, profile_add_on=date)



@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/contact/')
def contact():
  """Render webpage contact"""
  return render_template('contact.html')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
