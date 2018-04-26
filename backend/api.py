from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return 'Works!'

api.add_resource(Home, '/home')

if __name__ == '__main__':
    app.run(debug=True)