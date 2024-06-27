# Modified by fewrx
# Template credit: Antonio Sarosi

# Module for window layouts

from libqtile import layout
from libqtile.config import Match

from settings.options import Options

colors = Options.theme.get_theme()

layout_conf = {
    "border_focus": colors["focus"][0],
    "border_normal": colors["inactive"][0],
    "border_width": 2,  # orig: 1
    "margin": 8,  # orig: 4
}

monad_conf = {
    "ratio": 0.6,
    "change_size": 5,
    "change_ratio": 0.025,
}

# Uncomment a layout to enable it
# See keys.py for layout cycling keybinds
layouts = [
    layout.MonadTall(**layout_conf, **monad_conf),
    layout.Max(**layout_conf),
    layout.Stack(**layout_conf, num_stacks=2),
    layout.Floating(**layout_conf),
    layout.MonadThreeCol(**layout_conf, **monad_conf, main_centered=True, new_client_position="after_current"),
    layout.MonadWide(**layout_conf, **monad_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.RatioTile(**layout_conf),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="notification"),
    ],
    border_focus=colors["color4"][0],
)
