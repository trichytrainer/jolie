import os
import time
import docker

class DockerClient:
    def __init__(self):
        self.client = docker.from_env()
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.volumes = {
            self.current_path: {
                'bind': '/code',
                'mode': 'rw'
            }
        }

    def set_volumes(self, volume_definition):
        self.volumes = volume_definition

    def spawn_container(self, image, command, volumes=None, detach=False):
        return self.client.containers.run(
            image=image,
            command=command,
            volumes=self.volumes,
            detach=detach
        )

    def get_container_logs(self, container):
        stderr = ''
        stdout = ''

        for line in container.logs(stream=True, stderr=True, stdout=False):
            stderr += line.decode('utf-8')

        for line in container.logs(stream=True, stderr=False, stdout=True):
            stdout += line.decode('utf-8')

        return {
            'stderr': stderr,
            'stdout': stdout
        }

    def stop_container(self, container):
        container.stop()

    def clear_containers(self):
        return self.client.containers.prune()


"""
client = docker.from_env()
current_path = os.path.dirname(os.path.realpath(__file__))
image = "python:3.7-rc-stretch"

volumes = {
    current_path: {
        'bind': '/code',
        'mode': 'rw'
    }
}

container = client.containers.run(
    image=image,
    command="sh -c 'pip3 install pytest && cd code && python testrunner.py'",
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
"""