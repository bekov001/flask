from flask_restful import reqparse

parser = reqparse.RequestParser()
parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('is_finished', required=True, type=bool)

# news = User(
#             id=args['id'],
#             name=args['name'],
#             surname=args['surname'],
#             card=args['card'],
#             about=args['about'],
#             email=args['email'],
#             city_form=args['city_form']
#         )
src = ['job', 'work_size', "collaborators", "team_leader.id", "is_finished"]

for el in src:
    print("id=args['id'],".replace("id", el))