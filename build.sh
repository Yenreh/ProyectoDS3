#!/bin/bash

docker build -t yenreh/gestion_usuarios ./gestion_usuarios
docker build -t yenreh/auth ./auth
docker build -t yenreh/gestion_citas_medicas ./gestion_citas_medicas
docker build -t yenreh/api_gateway ./api_gateway
docker build -t yenreh/gestion_login ./gestion_login
#docker build -t yenreh/microfrontend ./microfrontend/login/project