#!/bin/bash

echo "Exiting Polybar"
killall polybar
echo "Reloading i3"
i3-msg restart
echo "Reloading rofi"
xrdb -merge ~/.Xdefaults
sleep 0.2
echo "Starting Polybar"
nohup polybar -c ~/.config/polybar/config main &> /dev/null &
echo "Restarting all instances of cava"
killall /home/joonatoona/Apps/bin/.libs/lt-cava &> /dev/null
echo "Reloading cmus"
cmus-remote -C "colorscheme auto" &> /dev/null