#!/bin/bash
kubectl apply -f redis_db/redis.yml
kubectl apply -f user_postgres_db/postgres-deployment.yaml
kubectl apply -f gestion_usuarios/gestion-usuarios-deployment.yml
kubectl apply -f auth/auth-deployment.yml
kubectl apply -f gestion_citas_medicas/gestion-citas-medicas-deployment.yml

sleep 30

kubectl port-forward svc/redis-service 6379:6379
kubectl port-forward svc/postgres-service 5432:5432
kubectl port-forward svc/auth-service 3000:3000
kubectl port-forward svc/gestion-usuarios-service 8000:8000
 kubectl port-forward svc/gestion-citas-medicas-service 8001:8000