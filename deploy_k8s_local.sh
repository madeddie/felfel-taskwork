#!/usr/bin/env bash
#
# This script builds the container locally and deploys the required k8s resources
######

if [[ $1 == "delete" ]]; then
  kubectl delete -f k8s/ingress.yml
  kubectl delete -f k8s/service.yml
  kubectl delete -f k8s/deployment.yml
else
  docker build -t felfel-taskwork:latest .
  kubectl apply -f k8s/deployment.yml
  kubectl apply -f k8s/service.yml
  kubectl apply -f k8s/ingress.yml
fi
