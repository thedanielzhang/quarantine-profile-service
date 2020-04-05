import json

from flask_restful import Resource, fields, abort, marshal_with, reqparse
from flask import Response

from profile_dao import ProfileDao 
from db_manager.db_utils import sql_query, sql_edit_insert, sql_delete, sql_query2

parser = reqparse.RequestParser()
parser.add_argument('userID', type=string, help='String userID of profile')
parser.add_argument('name', type=string, help='Full name of profile')

class Profile(Resource):

    def get(self, profile_id):
        results = sql_query2('''SELECT * FROM Profiles WHERE ProfileID = (?)''', (profile_id,))

        js = json.dumps( [dict(ix) for ix in results] )
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    def delete(self, profile_id):
        sql_delete('''DELETE FROM Profiles WHERE ProfileID = (?)''', (profile_id,))

    def put(self, profile_id):
        args = parser.parse_args()

        dao = ProfileDao(user_id=args['userID'], name=args['name']) # we should standardize between user_id and userID and userId

        profile_id = id(dao)

        user_id = args['userID']
        name = args['name']
        sql_edit_insert('''INSERT INTO Profiles (PantryID, Latitude, Longitude) VALUES (?, ?, ?)''', (profile_id, user_id, name))
        return 201

