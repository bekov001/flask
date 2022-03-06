import flask
from flask import jsonify

from data import db_session
from data.users import Jobs

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'work_size', "collaborators", "team_leader.id", "is_finished"))
                 for item in news]
        }
    )