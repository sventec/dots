# Options referenced in other parts of the configuration
# Values that may be hardware/machine specific, configurable per system, etc.
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paths:
    # Paths used in the config
    home = Path.home()
    # Absolute path to qtile config directory
    qtile = home / ".config/qtile"
    rofi_scripts = home / ".config/rofi/scripts"

    # @override
    # def __getattribute__(self, name: str, /) -> str:
    #     attr = dataclass.__getattribute__(self, name)
    #     if isinstance(attr, Path):
    #         return attr.as_posix()
    #     return str(attr)

    @classmethod
    def path(cls, path: str) -> str:
        return getattr(cls, path).as_posix()


@dataclass(frozen=True)
class KeyOptions:
    # Options specific to the settings.keys settings submodule
    mod = "mod4"
    term = "kitty"
    backup_term = "urxvt"


class Theme:
    """A custom theme, as defined in `themes/<theme>.json`.

    To set the desired theme, do not modify this class directly.
    Instead, configure the `theme` attribute of `Options` below.

    Example:
       ```python
       class Options:
           ...
           theme = Theme("everforest")
       ```
    """

    theme_path: Path
    theme: dict[str, list[str]]

    def __init__(self, theme: str) -> None:
        # reference Paths class directly here, as Options doesn't exist yet when the
        # theme is initialized (as an attribute of Options)
        self.theme_path = Path(Paths.qtile / f"themes/{theme}.json")

        if not self.theme_path.is_file():
            err = f"Cannot set theme, {self.theme_path} does not exist, or is not a file."
            raise FileNotFoundError(err)

        self.theme = json.loads(self.theme_path.read_text())

    def get_theme(self):
        """Get the theme's colors as a dictionary."""
        return self.theme


@dataclass(frozen=True)
class Options:
    """Configurable qtile options.

    Attributes:
        keys: Access KeyOptions. Do not change this, instead modify KeyOptions directly.
        paths: Access Paths. Do not change this, instead modify Paths directly.
        theme: Theme for status bar, etc. One of the filenames (without `.json`) in `themes/`.
    """

    keys = KeyOptions()
    paths = Paths()
    theme = Theme("everforest")
