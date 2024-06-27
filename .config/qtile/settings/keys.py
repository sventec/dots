# Modified by fewrx
# Template credit: Antonio Sarosi

# Module for creation of keybinds

from libqtile import qtile
from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from settings.options import Options

# shorter mod since it's in every bind
mod = Options.keys.mod

keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
        # ------------ Window Configs ------------
        # Switch between windows in current stack pane
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        ([mod], "i", lazy.layout.next()),
        ([mod], "o", lazy.layout.previous()),
        # Change window sizes (MonadTall)
        ([mod, "shift"], "l", lazy.layout.grow()),
        ([mod, "shift"], "h", lazy.layout.shrink()),
        # addition: normalize layout
        ([mod, "control"], "n", lazy.layout.normalize()),
        ([mod, "shift"], "n", lazy.group.prev_window()),
        ([mod], "n", lazy.group.next_window()),
        ([mod], "m", lazy.layout.maximize()),
        # Toggle floating
        ([mod, "shift"], "f", lazy.window.toggle_floating()),
        # Toggle fullscreen
        ([mod, "control"], "f", lazy.window.toggle_fullscreen()),
        # Flip side of main window (XMonadTall)
        ([mod], "f", lazy.layout.rotate(), lazy.layout.flip()),
        # Move windows up or down in current stack
        ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        # Toggle between different layouts as defined below
        ([mod], "Tab", lazy.next_layout()),
        ([mod, "shift"], "Tab", lazy.prev_layout()),
        # Kill window
        ([mod], "w", lazy.window.kill()),
        # Switch groups
        ([mod, "control"], "l", lazy.screen.next_group(skip_empty=True)),
        ([mod, "control"], "h", lazy.screen.prev_group(skip_empty=True)),
        ([mod], "grave", lazy.screen.toggle_group()),
        # Toggle scratchpad dropdown terminal
        ([mod], "d", lazy.group["scratchpad"].dropdown_toggle("term")),
        # Switch focus of monitors
        ([mod], "period", lazy.next_screen()),
        ([mod], "comma", lazy.prev_screen()),
        # Restart Qtile
        ([mod, "control"], "r", lazy.restart()),
        ([mod, "control"], "q", lazy.shutdown()),
        # ------------ App Configs ------------
        # Menu
        #  ([mod], "space", lazy.spawn("rofi -show drun -lines 6")),
        # adi1090x/rofi script launcher_text
        ([mod, "shift"], "space", lazy.spawn(str(Options.paths.rofi_scripts / "launcher_t4"))),
        # ([mod, "shift"], "space", lazy.spawn("rofi -show drun -modi drun")),
        ([mod], "space", lazy.spawn("dmenu_run -c -g 5 -bw 2 -sb '#BF616A' -sb '#2E3440'")),
        # Window Nav
        ([mod, "control"], "space", lazy.spawn("rofi -show window")),
        # Browser
        ([mod], "b", lazy.spawn("librewolf")),
        # File Explorer
        # ([mod], "e", lazy.spawn("pcmanfm")),
        ([mod], "e", lazy.spawn("thunar")),
        # Terminal
        ([mod], "Return", lazy.spawn(Options.keys.term)),
        ([mod, "shift"], "Return", lazy.spawn(Options.keys.backup_term)),
        # Screenshot
        ([mod], "s", lazy.spawn("scrot -e 'mv $f /home/fx/screenshots/")),
        ([mod, "shift"], "s", lazy.spawn("scrot -s")),
        ([], "Print", lazy.spawn("flameshot gui")),
        # Lock screen
        # ([mod, "shift"], "x", lazy.spawn("betterlockscreen -l blur")),
        ([mod, "shift"], "x", lazy.spawn("xset s activate")),
        # Lock screen & turn screen off (script)
        ([mod, "control"], "x", lazy.spawn([str(Options.paths.qtile / "screenoff.sh")])),
        # ([mod, "control"], "x", lazy.spawn("sleep 1;xset dpms force off")),
        # Show power menu (rofi-power-menu)
        ([mod], "x", lazy.spawn(str(Options.paths.rofi_scripts / "powermenu_t1"))),
        # ------------ Hardware Configs ------------
        # Volume
        # replaced by bindings from pa-applet
        # ([], "XF86AudioLowerVolume",
        #     lazy.spawn(f"{homedir}/scripts/volumeControl.sh down")),
        #  #  lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
        # ([], "XF86AudioRaiseVolume",
        #     lazy.spawn(f"{homedir}/scripts/volumeControl.sh up")),
        #  #  lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
        # ([], "XF86AudioMute",
        #  lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
        # Brightness
        #  ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
        #  ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
        # ([], "XF86MonBrightnessUp", lazy.spawn(f"{homedir}/scripts/brightnessControl.sh up")),
        ([], "XF86MonBrightnessUp", lazy.spawn(str(Options.paths.qtile / "scripts/brightnessControl.sh up"))),
        ([], "XF86MonBrightnessDown", lazy.spawn(Options.paths.qtile / "scripts/brightnessControl.sh down")),
        (["shift"], "XF86MonBrightnessUp", lazy.spawn(Options.paths.qtile / "scripts/brightnessControl.sh sup")),
        (["shift"], "XF86MonBrightnessDown", lazy.spawn(Options.paths.qtile / "scripts/brightnessControl.sh sdown")),
        ([], "XF86KbdBrightnessUp", lazy.spawn("brightnessctl --device='tpacpi::kbd_backlight' set +10%")),
        ([], "XF86KbdBrightnessDown", lazy.spawn("brightnessctl --device='tpacpi::kbd_backlight' set 10%-")),
    ]
]

# Normal key schema addendum
keys.append(
    # Program Key Chords
    KeyChord(
        [mod],
        "p",
        [
            Key([], "b", lazy.spawn("qutebrowser")),
            Key(["shift"], "b", lazy.spawn("librewolf")),
            Key(["control"], "b", lazy.spawn("firefox")),
            Key(["mod1"], "b", lazy.spawn("brave")),
            Key([], "c", lazy.spawn("code")),
            Key([], "z", lazy.spawn("zathura")),
            Key([], "p", lazy.spawn("bitwarden")),
            Key([], "e", lazy.spawn("emacs")),
            Key([], "t", lazy.spawn("teams")),
            Key([], "g", lazy.spawn(Options.keys.term + " lazygit")),
            Key([], "o", lazy.spawn("obsidian")),
        ],
        name="Shortcuts",
    )  # type: ignore[reportGeneralTypeIssues]
)

keys.append(
    # redshift key chords
    KeyChord(
        [mod],
        "r",
        [
            Key([], "1", lazy.spawn("redshift -O 4500")),
            Key([], "2", lazy.spawn("redshift -O 4000")),
            Key([], "3", lazy.spawn("redshift -O 3500")),
            Key([], "4", lazy.spawn("redshift -O 3000")),
            Key([], "5", lazy.spawn("redshift -O 3000 -b 0.5:0.5")),
        ],
        name="Redshift",
    )  # type: ignore[reportGeneralTypeIssues]
)

# Keys for programs with Wayland alternatives
if qtile.core.name == "x11":
    # Redshift
    keys.append(Key([mod, "shift"], "r", lazy.spawn("redshift -x")))
elif qtile.core.name == "wayland":
    keys.append(Key([mod, "shift"], "r", lazy.spawn("wlsunset -g 1.0")))
