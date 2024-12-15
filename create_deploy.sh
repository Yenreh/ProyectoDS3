#!/bin/bash
echo "Aplicando configuraciones de PostgreSQL..."
kubectl apply -f user_postgres_db/postgres-deployment.yaml
sleep 20

echo "Aplicando despliegues de backend..."
kubectl apply -f gestion_citas_medicas/gestion-citas-medicas-deployment.yml
kubectl apply -f gestion_usuarios/gestion-usuarios-deployment.yml
kubectl apply -f auth/auth-deployment.yml
kubectl apply -f comunicaciontiemporeal/comunicaciontiemporeal.yml
sleep 60

echo "Aplicando despliegue del API Gateway..."
kubectl apply -f api_gateway/api-gateway-deployment.yml
sleep 80

echo "Aplicando despliegue del frontend..."
kubectl apply -f frontend/frontend-deployment.yml
sleep 180

# Configurar port-forward para los servicios
echo "Redirigiendo puertos para el API Gateway (5000) (5173) (8080) (3001)..."
#kubectl port-forward service/loki-stack-grafana 3001:80&
kubectl port-forward svc/api-gateway-service 5000:5000 &
kubectl port-forward svc/frontend-service 5173:5173 &
kubectl port-forward svc/comunicaciontiemporeal 8080:8080 &





