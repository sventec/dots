# Qtile Config
# Template credit: Antonio Sarosi
# https://docs.qtile.org/en/v0.25.0/manual/config/index.html

# Primary file from which other config submodules are loaded

# ruff: noqa: F401
import subprocess

from libqtile import hook, qtile

from settings.groups import groups as _groups
from settings.keys import keys as _keys
from settings.keys import mod as _mod
from settings.layouts import floating_layout as _floating_layout
from settings.layouts import layouts as _layouts
from settings.mouse import mouse as _mouse
from settings.options import Options  # import global options for use in config
from settings.path import qtile_path as _qtile_path
from settings.screens import screens as _screens
from settings.widgets import extension_defaults as _extension_defaults
from settings.widgets import widget_defaults as _widget_defaults

# Remap keys (setxkbmap-like) on Wayland
if qtile.core.name == "wayland":
    from libqtile.backend.wayland import InputConfig

    # NOTE: wl_input_rules must be set before runtime. Use core's set_keymap to bind keys in Wayland during runtime.
    wl_input_rules = {
        "type:keyboard": InputConfig(kb_options="caps:escape"),  # Remap caps -> Esc
        # "type:touchpad": InputConfig(tap=True), # Enable tap to click on touchpad
    }


@hook.subscribe.startup_once
def autostart():
    if qtile.core.name == "x11":
        subprocess.Popen([Options.paths.qtile / "autostart.sh"])  # noqa: S603
    elif qtile.core.name == "wayland":
        subprocess.Popen([Options.paths.qtile / "autostart-wayland.sh"])  # noqa: S603


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
wmname = "LG3D"

# import configs from submodules into global namespace
groups = _groups
keys = _keys
mod = _mod
floating_layout = _floating_layout
layouts = _layouts
mouse = _mouse
qtile_path = _qtile_path
screens = _screens
extension_defaults = _extension_defaults
widget_defaults = _widget_defaults
