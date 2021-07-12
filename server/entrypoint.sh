#!/bin/bash -e
ip addr
export FLASK_APP=vsu_server.py
export FLASK_ENV=development
flask run --host 0.0.0.0
