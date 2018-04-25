import os
import docker

client = docker.from_env()

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
    command="sh -c 'cd code/tmp && python usercode.py' ",
    volumes=volumes,
    detach=True
)

for line in container.logs(stream=True):
    print(line.decode('utf-8'))