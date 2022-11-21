#!/bin/sh

sed -i "s/latest/${CLIENT_VERSION}/g" docker-compose.yaml
docker-compose up -d --build
