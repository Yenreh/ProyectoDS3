#!/bin/bash

docker build -t yenreh/gestion_usuarios ./gestion_usuarios
docker build -t yenreh/auth ./auth
docker build -t yenreh/gestion_citas_medicas ./gestion_citas_medicas