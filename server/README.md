# DCC-VSU Server

## Pre-Requisites
1. [Docker](https://www.docker.com/) should be running already if you want to 
   run the webserver isolated in a docker container

## Quick Start
### Standalone
1. ```./vsu_server.py```
### Docker
1. bash shell 
   1. ```./docker_build.sh```
   1. ```./docker_run_server.sh```
1. other
   1. ```docker build -t ehn/dcc-vsu .```
   1. ```docker run --rm -p 9010:5000 ehn/dcc-vsu```


## Default Settings
### Port Mappings

By default port 9010 on host mapped to 5000 in the docker container with the
```-p 9010:5000``` argument to ```docker run```. The target port of 5000 is set in the docker, 
but feel free to map some other host port, as required.

Flask server app in the docker listens to any incoming IP (host: 0.0.0.0)
