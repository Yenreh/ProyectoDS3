
#!/bin/bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install loki-stack grafana/loki-stack
kubectl delete statefulset loki-stack --cascade=orphan
helm upgrade loki-stack grafana/loki-stack -f values.yaml
sleep 180