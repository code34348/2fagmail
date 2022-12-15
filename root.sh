#!/bin/sh
# script that runs as root
# The display number must be a desktop session valid, you can view with echo $DISPLAY
export PATH=$PATH:/home/code8/2fagmail/geckodriver
DISPLAY=:1 python /home/code8/2fagmail/logingmail.py &
