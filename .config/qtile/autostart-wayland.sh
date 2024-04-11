#!/bin/sh

# Remap caps lock to escape
# This has been implemented in config.py

# systray network
nm-applet &

# set wallpaper
~/.swaybg &

# start dunst
dunst &

# start caffeine-ng
# caffeine &

# autostart gnome keyring daemon
# (to unlock keyring for vscode)
# gnome-keyring-daemon --start &

# start xss-lock to manage lock screen
# xss-lock -- betterlockscreen -l blur &

# start Dropbox on login
# /usr/bin/dropbox &

# start syncthingtray on login
# Alternatively, just use the syncthing service:
# systemctl enable --now syncthing@$USER
# syncthingtray &

# start flameshot in background
# flameshot &
