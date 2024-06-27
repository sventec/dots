# Modified by fewrx
# Template credit: Antonio Sarosi

# Module for multimonitor support

import subprocess

from libqtile import bar, qtile
from libqtile.config import Screen
from libqtile.log_utils import logger

from .widgets import primary_widgets, secondary_widgets


def status_bar(widgets):
    # Widgets, thickness, opacity (0.92)
    # return bar.Bar(widgets, 24, opacity=1.0)
    return bar.Bar(widgets, 30)


screens = [Screen(top=status_bar(primary_widgets))]

if qtile.core.name == "x11":
    xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

    command = subprocess.run(
        xrandr,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    if command.returncode != 0:
        error = command.stderr.decode("UTF-8")
        logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
        connected_monitors = 1
    else:
        connected_monitors = int(command.stdout.decode("UTF-8"))

    if connected_monitors > 1:
        for _ in range(1, connected_monitors):
            screens.append(Screen(top=status_bar(secondary_widgets)))
elif qtile.core.name == "wayland":
    # FIXME: Actually detect connected monitors in wayland?
    connected_monitors = 1
else:
    connected_monitors = 1
