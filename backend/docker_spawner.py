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
    command="sh -c 'pip3 install pytest && cd code && ls && pytest ./tmp && RC=$? && echo $RC'",
    volumes=volumes,
    detach=True
)

print(client.containers.list())
full_trace = ''

for line in container.logs(stream=True):
    print(line.decode('utf-8').rstrip())
    full_trace += line.decode('utf-8')

print(full_trace)
container.stop()
deleted_containers = client.containers.prune()