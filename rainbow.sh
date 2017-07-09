#!/bin/bash

i3conf=~/.config/i3/config

change_colors() {
	sed -i -e "s/\$color\ \#.\{6\}/\$color\ \#$1/" $i3conf
	sed -i -e "s/\$color_2\ \#.\{6\}/\$color_2\ \#$2/" $i3conf
	sed -i -e "s/\$color_uf\ \#.\{6\}/\$color_uf\ \#$3/" $i3conf
	i3-msg reload &> /dev/null
}

change_term_colors() {
	echo "rgb($1,$2,$3)" > ~/.gtcolors
}

get_hex() {
	printf "%02x%02x%02x" $1 $2 $3
}

RED=255
GREEN=0
BLUE=0

while :; do
for i in `seq 1 255`; do
	let RED-=1
	let GREEN+=1
	let RED_D=RED-100
	if [ $RED_D -lt 0 ]; then RED_D=0; fi
	let GREEN_D=GREEN-100
	if [ $GREEN_D -lt 0 ]; then GREEN_D=0; fi
	HEX=$(get_hex $RED $GREEN $BLUE)
	HEX_DARK=$(get_hex $RED_D $GREEN_D $BLUE)
	change_colors $HEX "000000" $HEX_DARK
	change_term_colors $RED $GREEN $BLUE
done

for i in `seq 1 255`; do
        let GREEN-=1
        let BLUE+=1
        let GREEN_D=GREEN-100
        if [ $GREEN_D -lt 0 ]; then GREEN_D=0; fi
        let BLUE_D=BLUE-100
        if [ $BLUE_D -lt 0 ]; then BLUE_D=0; fi
        HEX=$(get_hex $RED $GREEN $BLUE)
        HEX_DARK=$(get_hex $RED $GREEN_D $BLUE_D)
        change_colors $HEX "000000" $HEX_DARK
	change_term_colors $RED $GREEN $BLUE
done

for i in `seq 1 255`; do
        let BLUE-=1
        let RED+=1
        let BLUE_D=BLUE-100
        if [ $BLUE_D -lt 0 ]; then BLUE_D=0; fi
        let RED_D=RED-100
        if [ $RED_D -lt 0 ]; then RED_D=0; fi
        HEX=$(get_hex $RED $GREEN $BLUE)
        HEX_DARK=$(get_hex $RED_D $GREEN $BLUE_D)
        change_colors $HEX "000000" $HEX_DARK
	change_term_colors $RED $GREEN $BLUE
done
done
