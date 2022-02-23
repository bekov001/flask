import os

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


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            "static", 'mars', filename
        ))
    items = os.listdir("static/mars")
    return render_template("list.html", form=form, items=items)


if __name__ == '__main__':
    app.debug = True
    app.run()