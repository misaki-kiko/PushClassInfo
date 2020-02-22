from flask import Flask, render_template, session, redirect, url_for, flash
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, FloatField
from wtforms.validators import Required
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_qrcode import QRcode
import db

app = Flask(__name__)
bootstrap = Bootstrap(app)

site_title = "钉钉课表推送"

@app.route('/')
def hello_world():
    return render_template('index.html', site_title=site_title)

@app.route('/list')
def list():
    return render_template('list.html', site_title=site_title, l=db.select_all())



@app.errorhandler(404)
def notFound(e):
    title = '404 Not Found'
    return render_template('404.html', e=e, title=title, site_title=site_title), 404

@app.errorhandler(500)
def InternalServerError(e):
    title = '500 Internal Server Error'
    return render_template('500.html', e=e, title=title, site_title=site_title), 500


if __name__ == '__main__':
    app.run()
