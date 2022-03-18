from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.users import Jobs
from src.parsers.job_parser import parser

src = ["id", 'job', 'work_size', "collaborators", "team_leader", "is_finished"]
def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(Jobs).get(news_id)
    if not news:
        abort(404, message=f"Job {news_id} not found")


class JobsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(Jobs).get(news_id)
        return jsonify({'job': news.to_dict(
            only=src)})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(Jobs).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=src) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = Jobs(
            id=args["id"],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            team_leader=args['team_leader'],
            is_finished=args['is_finished']
        )

        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})