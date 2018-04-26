from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from docker_spawner import DockerClient

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        c = DockerClient()
        container = c.spawn_container(
            image='python:3.7-rc-stretch',
            command="sh -c 'pip3 install pytest && cd code && python testrunner.py'",
            detach=True
        )
        logs = c.get_container_logs(container)
        return logs

api.add_resource(Home, '/home')

if __name__ == '__main__':
    app.run(debug=True)