#!/bin/bash

echo "Reloading i3"
i3-msg reload &> /dev/null &

echo "Reloading rofi"
xrdb -merge ~/.Xdefaults &

echo "Restarting all instances of cava"
killall /home/joonatoona/Apps/bin/.libs/lt-cava &> /dev/null &

echo "Reloading cmus"
cmus-remote -C "colorscheme auto" &> /dev/null &