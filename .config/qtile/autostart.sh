#!/bin/bash

# Remap caps lock to escape
setxkbmap -option caps:escape

# start picom
# picom -b --experimental-backends &
picom -b &

# start dunst
dunst &

# systray battery icon
# cbatticon -u 5 &

# systray network
nm-applet &

# systray volume
# volumeicon &
# (pa-applet also replaces volume controls in settings/keys.py)
# sleep 2; pa-applet &
pa-applet &
# volumeicon &

# set wallpaper
# nitrogen --restore &
# feh --bg-fill ~/walls/nord-koi.png
# feh --big-fill ~/walls/nord-the-great-wave.png
# feh --big-fill ~/walls/nord-wallpapers/nordic-obsession.png
~/.fehbg &

# start caffeine-ng
caffeine &

# autostart gnome keyring daemon
# (to unlock keyring for vscode)
# dbus-update-activation-environment DISPLAY XAUTHORITY WAYLAND_DISPLAY
# gnome-keyring-daemon --start --components=secrets &
gnome-keyring-daemon --start &

# start Dropbox on login
# /usr/bin/dropbox &

# start syncthingtray on login
# Alternatively, just use the syncthing service:
# systemctl enable --now syncthing@$USER
# Tray can also be used in conjunction with systemd
# syncthingtray &

# start flameshot in background
# flameshot &

# start xss-lock to manage lock screen
xss-lock -- betterlockscreen -l blur &
