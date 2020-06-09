#!/usr/bin/env bash

## Complete the following steps to get Docker running locally
DOCKERPATH="dsalazar10/cluster"

# Run service
docker run -it -p 80:80 --rm $DOCKERPATH