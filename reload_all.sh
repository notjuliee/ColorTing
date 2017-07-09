#!/bin/bash

echo "Reloading i3"
i3-msg reload &> /dev/null &

echo "Reloading rofi"
xrdb -merge ~/.Xdefaults &

echo "Restarting all instances of cava"
killall /usr/bin/cava &> /dev/null &

echo "Reloading cmus"
cmus-remote -C "colorscheme auto" &> /dev/null &

echo "Reloading twmn"
killall twmnd
nohup twmnd &> /dev/null &

sleep 1 && twmnc "chameleon.py done" &
echo "Done!"
