#!/bin/bash

while inotifywait -e close_write ~/.gtcolors; do
	dconf write /org/gnome/terminal/legacy/profiles:/:b1dcc9dd-5262-4d8d-a863-c897e6d979b9/foreground-color $(echo \'$(head -n 1 ~/.gtcolors)\')
	dconf write /org/gnome/terminal/legacy/profiles:/:b1dcc9dd-5262-4d8d-a863-c897e6d979b9/background-color $(echo \'$(tail -n 1 ~/.gtcolors)\')
done
