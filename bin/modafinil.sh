#!/bin/sh

# Run a loop that moves the mouse cursor slightly to prevent screen sleep
while true; do
    xdotool mousemove_relative 5 5
    sleep 60
done
