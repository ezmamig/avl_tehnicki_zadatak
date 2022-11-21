#!/bin/sh

sed -i "s/latest/${CLIENT_VERSION}/g" avl_client_deployment.yaml
sed -i "s/latest/${BACKEND_VERSION}/g" avl_backend_deployment.yaml

kubectl apply -f avl_client_deployment.yaml
kubectl apply -f avl_client_service.yaml
kubectl apply -f avl_backend_deployment.yaml
kubectl apply -f avl_backend_service.yaml
