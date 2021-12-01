#!/usr/bin/env python3
import subprocess


def build_env():
    cmd1 = 'python3 -m venv ./aocenv'
    subprocess.check_call(cmd1, shell=True)

    cmd2 = 'source aocenv/bin/activate'
    subprocess.check_call(cmd2, shell=True)

    cmd3 = 'python -m pip install -r requirements.txt'
    subprocess.check_call(cmd3, shell=True)

    cmd4 = 'python -m pip install --upgrade pip'
    subprocess.check_call(cmd4, shell=True)


if __name__ == '__main__':
    build_env()
