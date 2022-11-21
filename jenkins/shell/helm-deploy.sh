#!/bin/sh

cd helm_charts
sed -i "s/latest/${BACKEND_VERSION}/g" helm-deploy/values-backend.yaml
sed -i "s/latest/${CLIENT_VERSION}/g" helm-deploy/values-client.yaml
helm install avl-backend helm-deploy --values helm-deploy/values-backend.yaml
helm install avl-client helm-deploy --values helm-deploy/values-client.yaml
