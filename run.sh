#!/bin/bash
kubectl apply -f redis_db/redis.yml
kubectl apply -f user_postgres_db/postgres-deployment.yaml
kubectl apply -f gestion_usuarios/gestion-usuarios-deployment.yml

sleep 30

kubectl port-forward svc/redis-service 6379:6379
kubectl port-forward svc/postgres-service 5432:5432