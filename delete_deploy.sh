#!/bin/bash

kubectl delete pod redis-pod
kubectl delete pod redis-pod-2
kubectl delete pod postgres-pod
kubectl delete pod auth-pod
kubectl delete pod gestion-usuarios-pod
kubectl delete pod gestion-citas-medicas-pod
kubectl delete pod gestion-login-pod
kubectl delete pod api-gateway-pod
kubectl delete pod microfrontend-pod

kubectl delete service redis-service
kubectl delete service redis-service-2
kubectl delete service postgres-service
kubectl delete service auth-service
kubectl delete service gestion-usuarios-service
kubectl delete service gestion-citas-medicas-service
kubectl delete service gestion-login-service
kubectl delete service api-gateway-service
kubectl delete service microfrontend-service
