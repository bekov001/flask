import flask
from flask import jsonify, request

from data import db_session
from data.users import Jobs

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)

src = ("id", 'job', 'work_size', "collaborators", "team_leader", "is_finished")
@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=("id", 'job', 'work_size', "collaborators", "team_leader.id", "is_finished"))
                 for item in news]
        }
    )


@blueprint.route('/api/job/<int:id>')
def get_news_one(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(id)
    if news:
        return jsonify(
            {
                'job':
                    news.to_dict(only=('job', 'work_size', "collaborators", "team_leader.id", "is_finished"))

            }
        )
    return "404"


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'work_size', "collaborators", "team_leader.id", "is_finished"]):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    user = db_sess.query(Jobs).get(request.json["id"])
    if not user:
        news = Jobs(
            id=request.json["id"],
            job=request.json['job'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            is_finished=request.json['is_finished'],
            team_leader=request.json['team_leader.id']
        )
        db_sess.add(news)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    return jsonify({"error": "Id already exists"})


@blueprint.route('/api/jobs/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(news_id)
    if not news:
        return jsonify({'error': 'Not found'})
    db_sess.delete(news)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/job/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    db_sess = db_session.create_session()
    # jobs = session.query(Jobs).get(job_id)
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in src for key in
                request.json.keys()):
        return jsonify({'error': 'Bad request'})
    job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    if not job:
        return jsonify({'error': 'Not found'})
    if isinstance(request.json.get('id', str), int) and db_sess.query(Jobs).filter(Jobs.id == request.json["id"]).first():
        return jsonify({'error': 'this id is exists'})
    if job:
        for el in src:
            if request.json.get(el, False) or isinstance(request.json.get(el, str), int):
                setattr(job, el, request.json[el])

    db_sess.commit()
    return jsonify({'success': 'OK'})