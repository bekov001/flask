from random import choice

from flask import Flask, redirect, render_template, request, abort
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash
from wtforms import EmailField, PasswordField, SubmitField, StringField, \
    BooleanField, IntegerField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user, \
    current_user
from data import db_session
from data.category import Category
from data.news import Department
from data.users import MarsUser, Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(MarsUser).get(user_id)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class AddDepartForm(FlaskForm):
    title = StringField('Department Title', validators=[DataRequired()])
    chief = IntegerField('Chief ID', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = EmailField('Department Email', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    surname = StringField("surname", validators=[DataRequired()])
    card = StringField("card", validators=[DataRequired()])
    about = StringField("about", validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class AddJobForm(FlaskForm):
    job = StringField('Job Title', validators=[DataRequired()])
    team_leader = IntegerField('Team Leader id', validators=[DataRequired()])
    work_size = StringField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')

    submit = SubmitField('Submit')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(MarsUser).filter(MarsUser.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = MarsUser()
        user.email = form.email.data
        user.name = form.name.data
        user.surname = form.surname.data
        user.card = form.card.data
        user.about = form.about.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template('register.html', title='Авторизация', form=form)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(MarsUser).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template("index.html", jobs=jobs, names=names)


@app.route('/add_depart', methods=['GET', 'POST'])
def add_depart():
    add_form = AddDepartForm()
    message=""
    if add_form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(MarsUser).filter(
            MarsUser.id == add_form.chief.data).first()
        if user:
            depart = Department(
                title=add_form.title.data,
                chief=add_form.chief.data,
                members=add_form.members.data,
                email=add_form.email.data
            )
            session.add(depart)
            session.commit()
            return redirect('/')
        message = "Неверный шеф"
    return render_template('add_depart.html', title='Adding a Department', form=add_form, message=message)


@app.route("/departments")
def depart():
    session = db_session.create_session()
    departments = session.query(Department).all()
    users = session.query(MarsUser).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template("lists.html", departments=departments, names=names, title='List of Departments')


@app.route('/departments/<int:id>', methods=['GET', 'POST'])
@login_required
def depart_edit(id):
    form = AddDepartForm()
    if request.method == "GET":
        session = db_session.create_session()
        depart = session.query(Department).filter(Department.id == id,
                                                  (Department.chief == current_user.id) | (
                                                          current_user.id == 1)).first()
        if depart:
            form.title.data = depart.title
            form.chief.data = depart.chief
            form.members.data = depart.members
            form.email.data = depart.email
        else:
            abort(404)
    if form.validate_on_submit():
        session = db_session.create_session()
        depart = session.query(Department).filter(Department.id == id,
                                                  (Department.chief == current_user.id) | (
                                                          current_user.id == 1)).first()
        if depart:
            depart.title = form.title.data
            depart.chief = form.chief.data
            depart.members = form.members.data
            depart.email = form.email.data
            session.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('add_depart.html', title='Department Edit', form=form)


@app.route('/depart_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def depart_delete(id):
    session = db_session.create_session()
    depart = session.query(Department).filter(Department.id == id,
                                              (Department.chief == current_user.id) | (
                                                      current_user.id == 1)).first()
    if depart:
        session.delete(depart)
        session.commit()
    else:
        abort(404)
    return redirect('/departments')


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    add_form = AddJobForm()
    message=""
    if add_form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(MarsUser).filter(
            MarsUser.id == add_form.team_leader.data).first()
        if user:
            jobs = Jobs(
                job=add_form.job.data,
                team_leader=add_form.team_leader.data,
                work_size=add_form.work_size.data,
                collaborators=add_form.collaborators.data,
                is_finished=add_form.is_finished.data
            )
            jobs.categories.append(choice([category, category1]))
            db_sess.add(jobs)
            db_sess.commit()
            return redirect('/')
        message = "Неверный тимлид"
    return render_template('add_job.html', title='Adding a job', form=add_form, message=message)


@app.route('/job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = AddJobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs and (current_user.id == 1 or current_user.id == jobs.team_leader):
            form.job.data = jobs.job
            form.team_leader.data = jobs.team_leader
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
        else:
            return "Страница не найдена либо у вас нет прав"
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs:
            jobs.job = form.job.data
            jobs.team_leader = form.team_leader.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_job.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if jobs and (current_user.id == 1 or current_user.id == jobs.team_leader):
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


def main():
    app.debug = True
    app.run()


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/mars.db")
    category = Category()
    category.name = "high"
    category1 = Category()
    category.name = "low"
    main()