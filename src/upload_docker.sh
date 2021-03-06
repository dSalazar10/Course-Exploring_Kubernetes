#!/bin/bash
# This file buils, tags and uploads an image to Docker Hub

# Create dockerpath
DOCKERPATH="dsalazar10/cluster"

# Authenticate
docker login

# Build image and add a descriptive tag
docker build -t $DOCKERPATH .

# Push image to a docker repository
docker push $DOCKERPATH