#!/bin/bash

while inotifywait -e close_write ~/.gtcolors; do
	dconf write /org/gnome/terminal/legacy/profiles:/:6f42fd60-c298-4dd0-852d-f8f4a4577078/foreground-color $(echo \'$(head -n 1 ~/.gtcolors)\')
	dconf write /org/gnome/terminal/legacy/profiles:/:6f42fd60-c298-4dd0-852d-f8f4a4577078/background-color $(echo \'$(tail -n 1 ~/.gtcolors)\')
done
