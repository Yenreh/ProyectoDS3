#!/bin/bash

kubectl delete pod redis-pod
kubectl delete pod postgres-pod
kubectl delete pod auth-pod

kubectl delete service redis-service
kubectl delete service postgres-service
kubectl delete service auth-service
