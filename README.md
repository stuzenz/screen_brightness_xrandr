# Hotkey extensions to control xrandr --brightness for your monitors

I thought this might be useful for someone. The below is probably a 10 minute tutorial for setting up the capability.

The below code gives you an extra 10 grades of brightness for each level you get with the physical brightness key on your computer. The code works for both your main monitor or a secondary monitor that you may have set as primary

Versus only using the built-in Thinkpad physical brightness keys (which you can continue to use) - you will get:

- extra sensitivity/ability to make the screen dimmer; and
- the hotkeys you set will work on your other HDMI/DP/usb-c monitors as well;
- personally, one area when I will use this is when I want my primary (DP/HDMI) monitor to be very dim for playing music/podcasts to mybigger speakers. It saves me having to fiddle with the monitor buttons. With that said, having played with it for 5 minutes, it seemsthere is still some back light that is not faded completely away when compared to the what my external monitor buttons can manipulate.

There will be plenty of ways to do this - but I thought this would be a nice simple piece of code so I decided to write it myself.

- This works on X11 (not wayland). You can check what you are running through `echo $XDG_SESSION_TYPE`
- It relies on using xbindkeys to do key bindings to the scripts

The files you will have at the end of this

- `/home/stuart/.xbindkeysrc`;
- `/home/stuart/.xprofile # an addition to this file - or create it if it does not exist`;
- `/home/stuart/bin/screen_brighten.py`;
- `/home/stuart/bin/screen_dim.py`;
- `/home/stuart/bin/screen_reset.py`;
- `/home/stuart/bin/screen_full_dim.py`;
- `/home/stuart/.xrandr_brightness_state`

Feel free to change the configuration of course, but for myself I have the following hotkeys - as stated above they work independently of the settings for your physical brightness keys.

- Alt + mic mute (alt-mod-f4) == full dim;
- Alt + screen dim (alt-mod-f5) == 10% dim screen;
- Alt + screen brighten (alt-mod-f6) == 10% brighten screen;
- Alt + project (alt-mod-f7) == brightness back to 100%

* A quick side note

This capability is using xrandr --brightness to make the change. I now have a better understanding of what xrandr --brightness does than what I did before I wrote the below code.

The flag xrandr --brightness doesn't actually change the brightness of your monitor, it just applies a filter to the colors so they look brighter or darker. Although this code works, I would like to improve it. If I find a good generic way to manipulate screen back light (including connected screens) from the terminal, I might go ahead and enhance this code to take advantage of both approaches.

The documentation states the following:

> --brightness brightness - multiply the gamma values on the crtc currently attached to the output to specified floating value. Useful for overly bright or overly dim outputs. However, this is a software only modification, if your hardware has support to actually change the brightness, you will probably prefer to use xbacklight.

I should note the code below has thresholds in place so that you cannot go below the brightness thresholds of 0 and 1.

​

## Steps

### 1. Install and set up xbindkeys

For archlinux

pacman -S xbindkeys

### 2. Move the dot files to your home directory

Before blindly copying these 3 files just confirm they do not exist. 
If they do exist, only edit in the relevant contents

- `.xbindkeysrc`

```
"/home/stuart/bin/screen_dim.py"
  Alt + XF86MonBrightnessDown

"/home/stuart/bin/screen_brighten.py"
  Alt + XF86MonBrightnessUp

"/home/stuart/bin/screen_full_dim.py"
  Alt + XF86AudioMicMute

"/home/stuart/bin/screen_reset.py"
  Alt + XF86Display
```

- `.xrandr_brightness_state`

```
1
```

- `.xprofile`

```
#Start xbindkeys
xbindkeys
```

### 3. Finish setting the xbindkeys up

`xbindkeys --poll-rc`

### 3. Copy the scripts from the `bin` directory

Copy the scripts to `/home/[YOUR_USER_NAME]/bin`

## Finally
That should be enough to get it working. If it doesn't work you might want to check if you are using Xorg or wayland - this will only work on Xorg.

Double check that you are using X11 by running

echo $XDG_SESSION_TYPE