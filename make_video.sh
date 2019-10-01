#!/bin/bash

ffmpeg -framerate 20 -i frames/%04d.png -c:v libx264 -r 30 -pix_fmt yuv420p -b:v 10M out.mp4