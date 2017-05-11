#!/usr/bin/env python

from sys import argv
import os
import re
import serial

rofi = ""
dir_path = os.path.dirname(os.path.realpath(__file__))
home_dir = os.path.expanduser("~")


def applyRazer(r, g, b):
    os.system(
        "echo -n -e \"\\x%s\\x%s\\x%s\" > /sys/bus/hid/drivers/razerkbd/0003:1532:0209.0003/matrix_effect_static"
        % (r, g, b))


def applyi3(primary, secondary):
    i3conf = open("%s/.config/i3/config" % home_dir).read()
    i3conf = re.sub(r"set \$color #.{1,6}", "set $color #%s" % primary, i3conf)
    i3conf = re.sub(r"set \$color_uf #.{1,6}", "set $color_uf #%s" % secondary,
                    i3conf)
    with open("%s/.config/i3/config" % home_dir, 'w') as file:
        file.write(i3conf)


def applyPolybar(primary, secondary, background):
    polybarConf = open("%s/.config/polybar/config" % home_dir).read()
    polybarConf = re.sub(r"primary = #.{1,6}", "primary = #%s" % primary,
                         polybarConf)
    polybarConf = re.sub(r"secondary = #.{1,6}", "secondary = #%s" % secondary,
                         polybarConf)
    polybarConf = re.sub(r"background = #.{1,6}", "background = #%s" % background,
                         polybarConf)
    polybarConf = re.sub(r"secondary = #.{1,6}", "secondary = #%s" % secondary,
                         polybarConf)
    with open("%s/.config/polybar/config" % home_dir, 'w') as file:
        file.write(polybarConf)


def applyCava(primary):
    cavaConf = open("%s/.config/cava/config" % home_dir).read()
    cavaConf = re.sub(r"foreground = '#.{1,6}'", "foreground = '#%s'" % primary,
                      cavaConf)
    with open("%s/.config/cava/config" % home_dir, 'w') as file:
        file.write(cavaConf)


def applyRofi(primary, secondary):
    rofiConf = open("%s/.Xdefaults" % home_dir).read()
    rofiConf = re.sub(r"rofi.color-normal: .+",
                      "rofi.color-normal: #111111,#%s,#222222,#444444,#%s" %
                      (primary, primary), rofiConf)
    rofiConf = re.sub(r"rofi.color-urgent: .+",
                      "rofi.color-urgent: #111111,#%s,#222222,#444444,#%s" %
                      (secondary, primary), rofiConf)
    rofiConf = re.sub(r"rofi.color-active: .+",
                      "rofi.color-active: #111111,#%s,#222222,#444444,#%s" %
                      (secondary, primary), rofiConf)
    with open("%s/.Xdefaults" % home_dir, 'w') as file:
        file.write(rofiConf)


def applyTerm(red, green, blue):
    with open("%s/.gtcolors" % home_dir, 'w') as file:
        file.write("rgb(%d,%d,%d)\nrgb(%d,%d,%d)" % (red[0], green[0], blue[0],red[2], green[2], blue[2]))


def applyFish(primary, secondary):
    colors = [
        "main %s" % primary, "command %s" % primary, "quote %s" % secondary,
        "redirection %s" % primary, "end %s" % secondary, "param %s" % primary,
        "comment %s" % secondary, "match %s" % secondary,
        "search_match %s" % secondary, "operator %s" % primary,
        "escape %s" % secondary, "cwd %s" % primary,
        "autosuggestion %s" % secondary
    ]

    for color in colors:
        os.system("fish -c \"set -Ux fish_color_%s\"" % color)


def applyLed(red, green, blue):
    with serial.Serial("/dev/ttyACM0") as ser:
        ser.write(b"%d %d %d\n" % ((255 - red), (255 - green), (255 - blue)))


def applyCmus(red, green, blue):
    primary = (36 * round(red[0] / 51)) + (6 * round(green[0] / 51)) + round(
        blue[0] / 51) + 16
    secondary = (36 * round(red[1] / 51)) + (6 * round(green[1] / 51)) + round(
        blue[1] / 51) + 16
    background = (36 * round(red[2] / 51)) + (6 * round(green[2] / 51)) + round(
        blue[2] / 51) + 16

    colors = [
        "cmdline_fg=%d" % primary,
        "info=%d" % primary,
        "separator=%d" % primary,
        "statusline_fg=%d" % primary,
        "titleline_fg=%d" % primary,
        "win_cur=%d" % primary,
        "win_cur_sel_bg=%d" % secondary,
        "win_cur_sel_fg=%d" % primary,
        "win_dir=%d" % primary,
        "win_fg=%d" % primary,
        "win_inactive_cur_sel_fg=%d" % primary,
        "win_inactive_sel_fg=%d" % primary,
        "win_sel_bg=%d" % secondary,
        "win_sel_fg=%d" % primary,
        "win_title_fg=%d" % primary,
        "cmdline_bg=%d" % background,
        "statusline_bg=%d" % background,
        "titleline_bg=%d" % background,
        "win_bg=%d" % background,
        "win_inactive_cur_sel_bg=%d" % background,
        "win_inactive_sel_bg=%d" % background,
        "win_sel_bg=%d" % background,
        "win_title_bg=%d" % background
    ]

    cmusConf = open("%s/.config/cmus/auto.theme" % home_dir).read()

    for color in colors:
        cmusConf = re.sub(r"set color_%s=.{1,3}" % color.split("=")[0],
                          "set color_%s" % color, cmusConf)

    with open("%s/.config/cmus/auto.theme" % home_dir, 'w') as file:
        file.write(cmusConf)


def main():
    red = [int(argv[1][:2], 16),int(argv[2][:2], 16),int(argv[3][:2], 16)]
    green = [int(argv[1][2:4], 16),int(argv[2][2:4], 16),int(argv[3][2:4], 16)]
    blue = [int(argv[1][4:6], 16),int(argv[2][4:6], 16),int(argv[3][4:6], 16)]

    print("Applying to keyboard")
    applyRazer(argv[1][:2], argv[1][2:4], argv[1][4:])

    print("Applying to i3")
    applyi3(argv[1], argv[2])

    print("Applying to Polybar")
    applyPolybar(argv[1], argv[2], argv[3])

    print("Applying to rofi")
    applyRofi(argv[1], argv[2])

    print("Applying to fish")
    applyFish(argv[1], argv[2])

    print("Applying to gnome_terminal")
    applyTerm(red, green, blue)

    print("Applying to cava")
    applyCava(argv[1])

    print("Applying to cmus")
    applyCmus(red, green, blue)

    print("Reloading Everything")
    os.system("%s/reload_all.sh" % dir_path)

    print("Applying to LED strip")
    applyLed(red[0], green[0], blue[0])


if len(argv) < 4:
    print("Usage: %s <Primary Color> <Secondary Color> <Background Color>" % argv[0])
else:
    main()
