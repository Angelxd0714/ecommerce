from base import *
from flask import jsonify
from validate_user.validate import Login


api.add_resource(Login,'/login')

if __name__ == '__main__':
    try:
        app.run(debug=True,port=6000)
    except Exception as e:
         raise jsonify({'error': str(e)})