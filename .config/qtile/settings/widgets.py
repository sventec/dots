# Modified by fewrx
# Template credit: Antonio Sarosi

# Module for configuring qtile bar and built-in widgets
# Required: Nerd Font or other support for icons from https://www.nerdfonts.com/cheat-sheet
# Optional: Use of OpenWeather widget requires an OpenWeather API key as environment variable OPENWEATHER_API_KEY
#           This environment variable can be set in e.g. .zshenv

import os

from libqtile import widget, qtile
from .theme import colors


BASE_FONTSIZE = 14


def base(fg='text', bg='dark'):
    return {'foreground': colors[fg], 'background': colors[bg]}


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


# fontsize + 2
def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(**base(fg, bg),
                          fontsize=fontsize,
                          text=text,
                          padding=3)


# fontsize
def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="|",
        fontsize=14,
        padding=2)


def workspaces():
    return [
        separator(),
        # fontsize + 5
        widget.GroupBox(**base(fg='light'),
                        font='UbuntuMono Nerd Font',
                        fontsize=19,
                        margin_y=3,
                        margin_x=0,
                        padding_y=8,
                        padding_x=4,
                        borderwidth=1,
                        active=colors['active'],
                        inactive=colors['inactive'],
                        rounded=True,
                        highlight_method='block',
                        urgent_alert_method='block',
                        urgent_border=colors['urgent'],
                        this_current_screen_border=colors['focus'],
                        this_screen_border=colors['grey'],
                        other_current_screen_border=colors['dark'],
                        other_screen_border=colors['dark'],
                        disable_drag=True),
        separator(),
        widget.CurrentLayoutIcon(**base(fg='focus'), scale=0.5),
        # fontsize - 2
        widget.CurrentLayout(**base(fg='focus'), fontsize=12),
        separator(),
        # fontsize - 2
        widget.WindowName(**base(fg='focus'), fontsize=12, padding=5),
        separator(),
    ]


# Widgets you wish to appear on all statusbars (primary and secondary)
common_widgets = [
    *workspaces(),
    separator(),
    widget.Chord(**base(fg='focus')),
    # fontsize - 2
    widget.Net(**base(fg='focus'), fontsize=12, interface='wlp61s0', padding=5,
               format='{down} ↓↑ {up}'),
    # fontsize - 2
    widget.Wlan(**base(fg='focus'), fontsize=12, padding=5, interface='wlp61s0',
                format='{essid} {percent:2.0%}'),
    widget.CheckUpdates(
        distro='Arch_checkupdates',
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        display_format='upd: {updates}',
        update_interval=1800, # In seconds, 1800 = 30 minutes
        padding=6
    ),
    powerline('color4', 'dark'),
    #  icon(fg="color4", text=' '),  # Icon: nf-fa-thermometer
    widget.ThermalSensor(**base(fg='color4'), metric=True, threshold=90),
    powerline('color3', 'dark'),
    # icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    # For thinkpad (you'll need to check interface name with `ip a`)
    # widget.Net(**base(bg='color3'), interface='wlp4s0'),
    #  icon(fg='color3', text='摒 '),
    widget.OpenWeather(
        **base(fg='color3'),
        cityid=5234372,
        app_key=os.getenv("OPENWEATHER_API_KEY"),
        metric=False,
        format='{main_temp}°{units_temperature} {humidity}% {weather_details}'
    ),
    powerline('color2', 'dark'),
    # This can be duplicated if your device has multiple batteries, just change battery=
    widget.Battery(**base(fg='color2'),
                   battery=0,
                   charge_char='',
                   discharge_char='',
                   full_char='',
                   unknown_char=''),
    powerline('color1', 'dark'),
    #  icon(fg="color1", fontsize=17, text=' '),  # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(fg='color1'), format='%H:%M:%S - %Y/%m/%d '),
    powerline('light', 'dark'),
    #  icon(bg='dark', text='墳 ', fg='light'),
    # widget.Volume(**base(bg='dark', fg='light'), padding=2),
    widget.PulseVolume(**base(fg='light'), step=5),
]

# Any primary statusbar-only widgets can be added either before or after the common widgets are added
primary_widgets = [
]

primary_widgets.extend(common_widgets)

if qtile.core.name == "x11":
    # Systray can only be spawned once (primary statusbar), see https://docs.qtile.org/en/latest/manual/ref/widgets.html#systray
    primary_widgets.append(widget.Systray(background=colors['dark'], padding=5))
elif qtile.core.name == "wayland":
    # Systray alternative for Wayland
    primary_widgets.append(widget.StatusNotifier(background=colors['dark'], padding=5))

secondary_widgets = [
]

secondary_widgets.extend(common_widgets)

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'padding': 1,
    'fontsize': 16,
}
extension_defaults = widget_defaults.copy()
