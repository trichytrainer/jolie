import os
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from docker_spawner import DockerClient
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
api = Api(app)
CORS(app)


@celery.task()
def start_exec_run(code):
    c = DockerClient()
    container = c.spawn_container(
        image='python:3.7-rc-stretch',
        command="sh -c 'pip3 install pytest && cd code && python testrunner.py'",
        detach=True
    )
    logs = c.get_container_logs(container)
    # os.remove('tmp/usercode.py')
    return logs, 200

class Home(Resource):
    def get(self):
        input = request.data
        print(input)
        file = open('tmp/usercode.py', 'w')
        file.write('''\
def add(a, b):
    return a+b
        ''')
        file.close()
        c = DockerClient()
        container = c.spawn_container(
            image='python:3.7-rc-stretch',
            command="sh -c 'pip3 install pytest && cd code && python testrunner.py'",
            detach=True
        )
        logs = c.get_container_logs(container)
        os.remove('tmp/usercode.py')
        return logs, 200

    def post(self):
        code = request.get_json()['code']
        file = open('tmp/usercode.py', 'w')
        file.write(code)
        file.close()
        finished_logs = start_exec_run.delay(code)
        return finished_logs.wait()


api.add_resource(Home, '/home')

if __name__ == '__main__':
    app.run(debug=True)
