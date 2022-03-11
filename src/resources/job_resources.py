from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.users import Jobs


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(Jobs).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class JobsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(Jobs).get(news_id)
        return jsonify({'news': news.to_dict(
            only=('title', 'content', 'user_id', 'is_private'))})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(Jobs).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})