# Modified by fewrx
# Template credit: Antonio Sarosi

# Module for managing groups/workspaces

from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.lazy import lazy

from .keys import keys, mod

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons:
# nf-fa-firefox,
# nf-fae-python,
# nf-dev-terminal,
# nf-fa-code,
# nf-oct-git_merge,
# nf-linux-docker,
# nf-mdi-image,
# nf-mdi-layers

groups = [
    Group(i) for i in [
        #"   ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", "   ",
        "   ",
        "   ",
        #  "   ",
        "   ",
        #  "  ",
        "   ",
        "   ",
        #  "   ",
        "   ",
    ]
]

groups.extend([
    ScratchPad("scratchpad", [
        DropDown("term", "kitty", opacity=0.8, height=0.6),
    ]),
])

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen(toggle=True)),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
        # addition: Send window to workspace N and switch to workspace
        Key([mod, "control"], actual_key, lazy.window.togroup(group.name),
            lazy.group[group.name].toscreen())
    ])
