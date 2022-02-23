import json
import os
from random import choice

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    FileField
from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '123123213'


class LoginForm(FlaskForm):
    file = FileField("Img", validators=[FileRequired()])
    submit = SubmitField('Войти')


@app.route('/member')
def index():
    data = json.load(open("static/data/data.json", encoding="utf8"))
    member = choice(data["members"])
    return render_template("answer.html", **member)


if __name__ == '__main__':
    app.debug = True
    app.run()