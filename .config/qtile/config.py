# Qtile Config
# Template credit: Antonio Sarosi
# https://docs.qtile.org/en/v0.25.0/manual/config/index.html

# Primary file from which other config submodules are loaded

# ruff: noqa: F401
import subprocess
from os import path

from libqtile import hook, qtile

from settings.groups import groups
from settings.keys import keys, mod
from settings.layouts import floating_layout, layouts
from settings.mouse import mouse
from settings.options import Options
from settings.path import qtile_path
from settings.screens import screens
from settings.widgets import extension_defaults, widget_defaults

# Remap keys (setxkbmap-like) on Wayland
if qtile.core.name == "wayland":
    from libqtile.backend.wayland import InputConfig
    # NOTE: wl_input_rules must be set before runtime. Use core's set_keymap to bind keys in Wayland during runtime.
    wl_input_rules = {
        "type:keyboard": InputConfig(kb_options="caps:escape"), # Remap caps -> Esc
        # "type:touchpad": InputConfig(tap=True), # Enable tap to click on touchpad
    }


@hook.subscribe.startup_once
def autostart():
    if qtile.core.name == "x11":
        subprocess.Popen([path.join(qtile_path, "autostart.sh")])
        # subprocess.call([path.join(qtile_path, 'autostart.sh')])
    elif qtile.core.name == "wayland":
        subprocess.call([path.join(qtile_path, "autostart-wayland.sh")])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
wmname = "LG3D"
