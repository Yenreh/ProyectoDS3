#!/bin/bash

#Build the images
docker build -t yenreh/gestion_usuarios ./gestion_usuarios
docker build -t yenreh/auth ./auth
docker build -t yenreh/gestion_citas_medicas ./gestion_citas_medicas
docker build -t yenreh/api_gateway ./api_gateway
docker build -t yenreh/gestion_login ./gestion_login
#docker build -t yenreh/microfrontend ./microfrontend/login/project

#Upload to Docker Hub
docker push yenreh/gestion_usuarios
docker push yenreh/auth
docker push yenreh/gestion_citas_medicas
docker push yenreh/api_gateway
docker push yenreh/gestion_login
#docker push yenreh/microfrontend