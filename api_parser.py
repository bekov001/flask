from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('card', required=True)
parser.add_argument('about', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)

a = """id=request.json["id"],
job=request.json['job'],
work_size=request.json['work_size'],
collaborators=request.json['collaborators'],
is_finished=request.json['is_finished'],
team_leader=request.json['team_leader.id']
"""
print(a.replace("\n", "").split("=")[::])