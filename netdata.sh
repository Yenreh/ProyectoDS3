#!/bin/bash

kubectl label nodes minikube role=netdata-parent
kubectl label nodes minikube-m02 role=netdata-child
kubectl label nodes minikube-m03 role=netdata-child

# Agregar el repositorio de Netdata
helm repo add netdata https://netdata.github.io/helmchart/

# Actualizar los repositorios
helm repo update

# Instalar Netdata con los valores proporcionados
helm install netdata netdata/netdata \
--set image.tag=edge \
--set parent.claiming.enabled=true \
--set parent.claiming.token=viVjoCZQFpl0rdRb3BsEC5Ab8vm8MK8oyEzNtmCAmAeFfRbUro5gWn_FfKpdslQsWlFAgXtOuahGiISWutHxOf0Rew7AcnMMzbNdT4mKji6ZREj6WZPJ5rbrnDfxt9U0OxQmNEk \
--set parent.claiming.rooms=4da01088-6f86-4740-9ca1-7a7521ed39b9 \
--set child.claiming.enabled=true \
--set logs.enabled=true \
--set logs.container_logs.enabled=true \
--set extraVolumes[0].name=logs \
--set extraVolumes[0].hostPath.path=/var/log/containers \
--set extraVolumeMounts[0].mountPath=/var/log/containers \
--set extraVolumeMounts[0].name=logs \
--set child.claiming.token=viVjoCZQFpl0rdRb3BsEC5Ab8vm8MK8oyEzNtmCAmAeFfRbUro5gWn_FfKpdslQsWlFAgXtOuahGiISWutHxOf0Rew7AcnMMzbNdT4mKji6ZREj6WZPJ5rbrnDfxt9U0OxQmNEk \
--set child.claiming.rooms=4da01088-6f86-4740-9ca1-7a7521ed39b9


# Desplegar Netdata usando valores personalizados
echo "Desplegando Netdata..."
helm upgrade -f netdata/override.yaml netdata netdata/netdata
