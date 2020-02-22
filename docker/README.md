# Docker Compose files

This directory contains scripts for installing Docker Compose and start/stop all the containers prepared previously in subprojects.
That is, if, for a sub project called ```$SUBPROJECT```, files ```$SUBPROJECT/Dockerfile*``` and ```$SUBPROJECT/docker-build.sh``` exist, the latter should be run.
After running ```docker-build.sh``` files for each relevant sub-project, ```docker-compose``` can start/stop the whole ecosystem of MLFabrique.

## Installing ```docker-compose``` on Linux
Run ```./install-docker-compose.sh``` script.

## Run the MLFabrique ecosystem
Having installed ```docker-compose```, the MLFabrique ecosystem can be started with
```./docker-compose-up.sh``` script (or ```./docker-compose-up-daemon.sh``` for daemon mode in the background).
Next, the ecosystem can be stopped with
```./docker-compose-down.sh``` script.
