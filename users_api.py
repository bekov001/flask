import flask
from flask import jsonify, request

from data import db_session
from data.users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)

src = ['id', 'name', 'surname', 'card', 'about', 'email', "city_form", "password"]

@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    news = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=src[:-1])
                 for item in news]
        }
    )


@blueprint.route('/api/user/<int:id>')
def get_user_one(id):
    db_sess = db_session.create_session()
    news = db_sess.query(User).get(id)
    if news:
        return jsonify(
            {
                'user':
                    news.to_dict(only=src[:-1])

            }
        )
    return "404"


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in src):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(request.json["id"])
    if not user:
        news = User(
            id=request.json['id'],
            name=request.json['name'],
            surname=request.json['surname'],
            card=request.json['card'],
            about=request.json['about'],
            email=request.json['email'],
            city_form=request.json['city_form']
        )
        news.set_password(request.json['password'])
        db_sess.add(news)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    return jsonify({"error": "Id already exists"})


@blueprint.route('/api/user/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(User).get(news_id)
    if not news:
        return jsonify({'error': 'Not found'})
    db_sess.delete(news)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    db_sess = db_session.create_session()
    # jobs = session.query(Jobs).get(job_id)
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                src):
        return jsonify({'error': 'Bad request'})
    edit_user = db_sess.query(User).filter(User.id == job_id).first()
    if not edit_user:
        return jsonify({'error': 'Not found'})
    if isinstance(request.json.get('id', False), int) and db_sess.query(User).filter(User.id == request.json["id"]).first():
        return jsonify({'error': 'this id is exists'})
    if edit_user:
        for el in src:
            if request.json.get(el, False) or isinstance(request.json.get(el, False), int):
                setattr(edit_user, el, request.json[el])

    db_sess.commit()
    return jsonify({'success': 'OK'})