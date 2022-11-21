#!/bin/sh

kubectl delete deployment.apps/avl-backend
kubectl delete deployment.apps/avl-client

kubectl delete service/avl-backend-api
kubectl delete service/avl-client-api
