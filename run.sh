#!/bin/bash
kubectl apply -f user_postgres_db/postgres-deployment.yaml
sleep 10
kubectl apply -f redis_db/redis.yml
kubectl apply -f redis_db/redis-2.yml
sleep 10
kubectl apply -f gestion_login/gestion-login-deployment.yml
kubectl apply -f gestion_citas_medicas/gestion-citas-medicas-deployment.yml
kubectl apply -f gestion_usuarios/gestion-usuarios-deployment.yml
kubectl apply -f auth/auth-deployment.yml
sleep 5
kubectl apply -f api_gateway/api-gateway-deployment.yml
sleep 10
kubectl apply -f microfrontend/microfrontend-deployment.yml
sleep 5
kubectl port-forward svc/api-gateway-service 5000:5000 &
kubectl port-forward svc/microfrontend-service 5173:5173 &