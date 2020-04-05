from flask_restful import Resource, fields, marshal_with

class ProfileDao(object):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name