from flask_restful import Resource, abort, reqparse
from controllers import checkSend
from flask import request

class Main(Resource):
    def get(self):
        return 'Mail backup running'

class sendMail(Resource):
    def get(self):
        return 'Email sending details are displayed here'

    def post(self):
        data = request.json
        # return (data['code'])
        return checkSend(data['code'])


