#!/bin/sh

docker rm -f avl-backend-api avl-client-api
docker rmi -f avl_client:${VERSION}
docker rmi -f avl_backend:${VERSION}