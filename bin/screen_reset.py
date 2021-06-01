#! /usr/bin/python
import os

# Used to reset the screen brightness
# Used with xbindkeys for hotkeys

stream=os.popen("xrandr | awk '/ primary/{print $1}'")
active_display = stream.read().rstrip()

stream=os.popen("echo $HOME")
home_path = stream.read().rstrip()

os.system('xrandr --output {} --brightness {}'.format(active_display,str(1)))

f = open('{}/.xrandr_brightness_state'.format(home_path), "w")
f.write(str(1))
f.close()