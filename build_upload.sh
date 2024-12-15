#!/bin/bash

#Build the images
docker build -t dylanfarkas/auth ./auth
docker build -t dylanfarkas/gestion_usuarios ./gestion_usuarios
docker build -t dylanfarkas/gestion_citas_medicas ./gestion_citas_medicas
docker build -t dylanfarkas/api_gateway ./api_gateway
docker build -t dylanfarkas/frontend ./Frontend
docker build -t dylanfarkas/comunicaciontiemporeal ./ComunicacionTiempoReal

#Upload to Docker Hub
docker push dylanfarkas/auth
docker push dylanfarkas/gestion_usuarios
docker push dylanfarkas/gestion_citas_medicas
docker push dylanfarkas/api_gateway
docker push dylanfarkas/frontend
docker push dylanfarkas/comunicaciontiemporeal

