import os
import subprocess
import sys


def create_virtualenv(env_name='venv'):
    subprocess.check_call([sys.executable, '-m', 'venv', env_name])


def install_requirements(env_name='venv'):
    subprocess.check_call(
        [os.path.join(env_name, 'Scripts', 'pip'), 'install', '-r', 'requirements.txt'])


if __name__ == '__main__':
    create_virtualenv()
    install_requirements()
