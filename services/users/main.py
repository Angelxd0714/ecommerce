from flask import Flask
from flask_restful import Api

from services.users.functions.userFunctions import UserFunctions

app = Flask(__name__)
api = Api(app)

api.add_resource(UserFunctions, '/users')

if __name__ == '__main__':
    app.run(debug=True)