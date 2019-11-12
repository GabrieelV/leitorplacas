#!/usr/bin/env bash

docker run --device=/dev/video0:/dev/video0 --net=host -it trabalho/openalpr /bin/sh
