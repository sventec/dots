# Qtile config

[Qtile](https://qtile.org/) config framework, originally based on the dotfiles of [Antonio Sarosi](https://github.com/antoniosarosi/dotfiles).

## Prerequisites

Qtile and *at least* the ubuntu mono nerd font must be installed:

```bash
sudo pacman -S qtile
yay -S nerd-fonts-ubuntu-mono
```

### Autostart Prerequisites

Make sure that the programs in [autostart.sh](autostart.sh) are installed or replaced with suitable alternatives.

The programs currently used are as follows:

- `setxkbmap`: Already installed on system. Used to remap Capslock to Escape. Remove this line to revert Capslock to the default behavior.
- `nm-applet`: Applet to display status of network provided by NetworkManager. Dropdown for selecting Wi-Fi networks, etc.
- `feh`: Used to set wallpaper. Can be replaced with `nitrogen`, etc.
- `picom`: Compositor, either picom or a compatible fork.
- `dunst`: Notification daemon.
- `xss-lock`: Optional, used to provide lockscreen functionality.
- `betterlockscreen`: Optional, used to provide lockscreen functionality.

### Optional Wayland Prerequisites

For Wayland support, install the following (XWayland is optional):

```bash
sudo pacman -S xwayland wayland wlroots
pip install pywayland pywlroots
```

Additionally, make sure all requirements in [autostart-wayland.sh](autostart-wayland.sh) are satisfied or replaced with suitable alternatives.

Then, launch `Qtile (Wayland)` from your display manager/greeter/etc.
Any X or Wayland-only options check the backend so no config files need to be modified to swap between Wayland/X.
See the bottom of [keys.py](settings/keys.py) for an example of this.

## Basic configueration

**WIP**

TODO: add basic configuration info after refactor

### Theme

...

### Hardware-specific

...

## Theme

Create a [theme](themes/README.md), or choose one of the available themes, and set the filename (without `.json`) in [config.json](config.json).
This will update the colors for the statusbar, window borders, etc.

## Config Structure

Although the config file names are relatively simple, short descriptions of each file found in `settings/` are included here:

- `groups.py`: Defines the groups/workspaces used by Qtile. Workspace icons are set here.
- `keys.py`: Keybinds for Qtile are set here. Key chords are also supported, see the existing config for examples.
- `layouts.py`: Defines which window layouts are available, comment/uncomment layouts to disable/enable.
- `mouse.py`: Enables some basic mouse support. Not much to change here.
- `path.py`: Small utility file to expose the config path. Not much to change here.
- `screens.py`: Defines the screens available to Qtile. Dynamically finds screens on X, screens must be manually configured here if using Wayland.
- `theme.py`: Utility file to load themes from `themes/*.json`. Don't set the theme in this file, that's done in `config.json`.
- `widgets.py`: Configuration for the builtin statusbar widgets. Some editing likely required here (network adapter name, OpenWeather API key).

