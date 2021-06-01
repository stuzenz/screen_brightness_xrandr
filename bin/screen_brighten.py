#! /usr/bin/python
import os

# Used to brighten the screen
# Used with xbindkeys for hotkeys

stream=os.popen("xrandr | awk '/ primary/{print $1}'")
active_display = stream.read().rstrip()

stream=os.popen("echo $HOME")
home_path = stream.read().rstrip()

with open('{}/.xrandr_brightness_state'.format(home_path), "r") as f:
    current_brightness_state = f.read()

current_brightness_state = float(current_brightness_state)
new_brighness_state = min(round(current_brightness_state + 0.1,1),1)

os.system('xrandr --output {} --brightness {}'.format(active_display,str(new_brighness_state)))

with open('{}/.xrandr_brightness_state'.format(home_path), "w") as f:
    f.write(str(new_brighness_state))
