from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('card', required=True)
parser.add_argument('about', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)