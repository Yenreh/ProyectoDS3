#!/bin/bash

#Build the images
docker build -t ervincaravaliibarra/auth ./auth
docker build -t ervincaravaliibarra/gestion_usuarios ./gestion_usuarios
docker build -t ervincaravaliibarra/gestion_citas_medicas ./gestion_citas_medicas
docker build -t ervincaravaliibarra/api_gateway ./api_gateway
docker build -t ervincaravaliibarra/frontend ./Frontend
docker build -t ervincaravaliibarra/comunicaciontiemporeal ./ComunicacionTiempoReal

#Upload to Docker Hub
docker push ervincaravaliibarra/auth
docker push ervincaravaliibarra/gestion_usuarios
docker push ervincaravaliibarra/gestion_citas_medicas
docker push ervincaravaliibarra/api_gateway
docker push ervincaravaliibarra/frontend
docker push ervincaravaliibarra/comunicaciontiemporeal

