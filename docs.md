# Using this on your system

## I AM IN NO WAY RESPONSIBLE FOR ANY ISSUES THAT MAY ARISE DURING THE USE OF THIS SCRIPT.
## DON'T BE AN IDIOT. BACK UP YOUR CONFIGS.
## THIS SCRIPT IS A WIP. BREAKING CHANGES WILL MOST LIKELY BE INTRODUCED. I WARNED YOU.

(Note: I'm assuming you're using either bash or fish on gnome-terminal)

Requires python3 and PySerial!

Make sure you edit `chameleon.py` and `reload_all.sh` and comment out everything that you don't have on your system.

For example, if you're using bash instead of fish comment out 
```python
print("Applying to fish")
applyFish(argv[1], argv[2])
```
in main.py, and ignore instructions for Fish in this document.

Check all the paths in `chameleon.py` and make sure they're correct for your system.

If you've followed all the instructions in this document and still can't get it to work, feel free to PM me [here](https://www.reddit.com/message/compose?to=joonatoona&subject=full_rgb)

## Special changes

### Polybar

Use the variables `background`, `primary`, and `secondary`.

The [colors] block of your config should look something like this:
```
[colors]
background = #000000
background-alt = ${colors.background}
primary = #ffffff
secondary = #dddddd
alert = #55FF0000
```

Make sure you start polybar with `polybar -c /path/to/config -r bar_name`

### gnome-terminal

Add this to `~/.gtcolors`
```
rgb(255,255,255)
rgb(0,0,0)
```

In the profile preferences for `gnome-terminal` check `Run command as a login shell` and `Run a custom command instead of my shell`

Set the custom command to 
```bash
bash -c '/home/joonatoona/src/ColorTing/term_colors.sh &> /dev/null & fish'
```
changing the path to wherever you cloned this repo, and fish to whatever your shell is.

### i3

In your i3 config, make sure all colors are using the variables `color` (Primary), `color_uf` (Secondary), and `color_2` (Background). Add this to the top:
```
set $color #ffffff
set $color_2 #222222
set $color_uf #dddddd
```

### cmus

Copy `auto.theme` from this repo to `~/.config/cmus/auto.theme`

### cava

Start cava with
```bash
while :; do
    cava
done
```

### LED Strip

Connect an LED strip to the arduino in this way:
```
Pin9: RED
Pin10: GREEN
Pin11: BLUE
5V: POWER
```

Then flash the sketch in this repo to the arduino.

Also change
```python
with serial.Serial("/dev/ttyACM0") as ser:
```
to the serial port your Arduino is connected to.

### Keyboard

(Only works with Razer keyboards as of now)

Change the path to point to your keyboard bus.
```
os.system(
        "echo -n -e \"\\x%s\\x%s\\x%s\" > /sys/bus/hid/drivers/razerkbd/0003:1532:0209.0003/matrix_effect_static"
        % (r, g, b))
```

### ROFI

Make sure these lines are in your `~/.Xdefaults`
```
rofi.color-normal: #111111,#ffffff,#222222,#444444,#ffffff
rofi.color-urgent: #111111,#dddddd,#222222,#444444,#ffffff
rofi.color-active: #111111,#dddddd,#222222,#444444,#ffffff
```

### Fish

Add
```
set -e -g fish_color_main
set -e -g fish_color_command
set -e -g fish_color_quote
set -e -g fish_color_redirection
set -e -g fish_color_param
set -e -g fish_color_comment
set -e -g fish_color_match
set -e -g fish_color_search_match
set -e -g fish_color_operator
set -e -g fish_color_escape
set -e -g fish_color_cwd
set -e -g fish_color_autosuggestion
set -e -g fish_color_end
```
to `~/.config/fish/config.fish`
