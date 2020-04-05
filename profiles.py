import json

from flask_restful import Resource, fields, abort, marshal_with, reqparse
from flask import Response

from profile_dao import ProfileDao
from db_manager.db_utils import sql_query, sql_edit_insert, sql_delete, sql_query2

parser = reqparse.RequestParser()
parser.add_argument('userID', type=str, help='String userID of profile')
parser.add_argument('name', type=str, help='Full name of profile')

class Profiles(Resource):

    def get(self):
        results = sql_query('''SELECT * FROM Profiles''')

        js = json.dumps( [dict(ix) for ix in results] )
        resp = Response(js, status=200, mimetype='application/json')
        return resp
    
    def post(self):
        args = parser.parse_args()

        dao = ProfileDao(user_id=args['userID'], name=args['name'])

        profile_id = id(dao)
        print(profile_id)

        user_id = args['userID']
        name = args['name']

        sql_edit_insert('''INSERT INTO Profiles (ProfileID, UserID, Name) VALUES (?, ?, ?)''', (profile_id, user_id, name))

        return 201

