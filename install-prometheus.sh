#!/bin/bash

# Agregar el repositorio de Grafana y actualizar
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Instalar Prometheus con Alertmanager, Node Exporter y Kube-State-Metrics, pero sin Grafana
helm install prometheus prometheus-community/kube-prometheus-stack \
  --set grafana.enabled=false

# Esperar 3 minutos para que los pods se inicialicen
sleep 180


