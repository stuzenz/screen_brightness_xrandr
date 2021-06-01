#! /usr/bin/python
import os

# Used to dim the screen
# Used with xbindkeys for hotkeys

stream=os.popen("xrandr | awk '/ primary/{print $1}'")
active_display = stream.read().rstrip()

stream=os.popen("echo $HOME")
home_path = stream.read().rstrip()

f = open('{}/.xrandr_brightness_state'.format(home_path), "r")
current_brightness_state = f.read()
f.close()

current_brightness_state = float(current_brightness_state)
new_brighness_state = max(round(current_brightness_state - 0.1,1),0)

os.system('xrandr --output {} --brightness {}'.format(active_display,str(new_brighness_state)))

f = open('{}/.xrandr_brightness_state'.format(home_path), "w")
f.write(str(new_brighness_state))
f.close()