#!/bin/bash

#This file plays the startup sound
if [ -f "/etc/sound/play" ]; then
  echo "Startup sound: On"
  #Old way:
  #omxplayer -o hdmi -b --vol -2000 /etc/sound/startup.mp3
  #New way:
  python3 /etc/sound/startup.py
else
  echo "Startup sound: Off"
fi