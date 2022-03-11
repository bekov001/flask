from flask import jsonify, request
from flask_restful import abort, Resource

from data import db_session
from data.users import Jobs, User
from api_parser import parser

src = ['id', 'name', 'surname', 'card', 'about', 'email', "city_form", "password"]


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(User).get(news_id)
    if not news:
        abort(404, message=f"User {news_id} not found")


class UserResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(Jobs).get(news_id)
        return jsonify({'user': news.to_dict(
            only=src[:-1])})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(Jobs).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=src[:-1]) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = User(
            id=args['id'],
            name=args['name'],
            surname=args['surname'],
            card=args['card'],
            about=args['about'],
            email=args['email'],
            city_form=args['city_form']
        )

        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})