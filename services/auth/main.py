from base import *
from flask import jsonify
from validate_user.validate import Login
from flask_cors import CORS

api.add_resource(Login,'/login')
CORS(app,origins=['http://localhost:4200'])
if __name__ == '__main__':
    try:
        app.run(debug=True,port=4000)
    except Exception as e:
         raise jsonify({'error': str(e)})