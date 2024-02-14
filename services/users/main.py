from base import *

api.add_resource(UserFunctions, '/users')

if __name__ == '__main__':
    app.run(debug=True)