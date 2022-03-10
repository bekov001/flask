from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.users import Jobs, User
from api_parser import parser


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(Jobs).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class UserResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(Jobs).get(news_id)
        return jsonify({'user': news.to_dict(
            only=('title', 'content', 'user_id', 'is_private'))})

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
        return jsonify({'news': [item.to_dict(
            only=('title', 'content', 'user.name')) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = User(
            name=args['title'],
            surname=args['content'],
            user_id=args['user_id'],
            is_published=args['is_published'],
            is_private=args['is_private']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})