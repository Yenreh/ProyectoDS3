#!/bin/bash

kubectl delete -f user_postgres_db/postgres-deployment.yaml
kubectl delete -f gestion_citas_medicas/gestion-citas-medicas-deployment.yml
kubectl delete -f gestion_usuarios/gestion-usuarios-deployment.yml
kubectl delete -f auth/auth-deployment.yml
kubectl delete -f api_gateway/api-gateway-deployment.yml
kubectl delete -f frontend/frontend-deployment.yml
