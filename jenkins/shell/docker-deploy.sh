#!/bin/sh

sed -i "s/latest/${VERSION}/g" docker-compose.yaml
docker-compose up -d --build
