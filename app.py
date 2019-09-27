from flask import Flask
from flask_restful import Api
from models import Main, sendMail


app = Flask(__name__)
api = Api(app)

api.add_resource(Main, '/')
api.add_resource(sendMail, '/mail')

if __name__ == '__main__':
    app.run(debug = True)