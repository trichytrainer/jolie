import os
import time
import docker

client = docker.from_env()
api_client = docker.APIClient()

image = "python:3.7-rc-stretch"
current_path = os.path.dirname(os.path.realpath(__file__))

volumes = {
    current_path: {
        'bind': '/code',
        'mode': 'rw'
    }
}

container = client.containers.run(
    image=image,
    command="sh -c 'pip3 install pytest && cd code && python tmp/testrunner.py'",
    volumes=volumes,
    detach=True
)

print(client.containers.list())

stderr = ''
stdout = ''

for line in container.logs(stream=True, stderr=True, stdout=False):
    stderr += line.decode('utf-8')

for line in container.logs(stream=True, stderr=False, stdout=True):
    stdout += line.decode('utf-8')

print('standardout: ' + stdout)
print('standarderr: ' + stderr)

container.stop()
deleted_containers = client.containers.prune()