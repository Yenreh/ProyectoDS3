#!/bin/bash

kubectl delete -f user_postgres_db/postgres-deployment.yaml
kubectl delete -f redis_db/redis.yml
kubectl delete -f redis_db/redis-2.yml
kubectl delete -f gestion_login/gestion-login-deployment.yml
kubectl delete -f gestion_citas_medicas/gestion-citas-medicas-deployment.yml
kubectl delete -f gestion_usuarios/gestion-usuarios-deployment.yml
kubectl delete -f auth/auth-deployment.yml
kubectl delete -f api_gateway/api-gateway-deployment.yml
#kubectl delete -f microfrontend/microfrontend-deployment.yml
