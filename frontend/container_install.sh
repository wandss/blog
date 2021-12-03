#!/bin/bash
# This script use a temporary container to create a local vue project using vue cli
# Doing so it won't be required to have node, npme, yar, vue installed locally.

docker run \
--rm \
--user "$(id -u):$(id -g)" \
-v "${PWD}:/$(basename `pwd`)" \
-w "/$(basename `pwd`)" \
-it \
node:lts-alpine \
sh -c "yarn global add @vue/cli && \
/home/node/.yarn/bin/vue create ."
