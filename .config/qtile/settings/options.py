# Options referenced in other parts of the configuration
# Values that may be hardware/machine specific, configurable per system, etc.

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Paths:
    # Paths used in the config
    home = Path.home().as_posix()
    # Absolute path to qtile config directory
    qtile = home / Path(".config/qtile")
    rofi_scripts = home / Path(".config/rofi/scripts")

    # @override
    # def __getattribute__(self, name: str, /) -> str:
    #     attr = dataclass.__getattribute__(self, name)
    #     if isinstance(attr, Path):
    #         return attr.as_posix()
    #     return str(attr)

    @classmethod
    def path(cls, path: str) -> str:
        return getattr(cls, path).as_posix()


@dataclass
class KeyOptions:
    # Options specific to the settings.keys settings submodule
    mod = "mod4"
    term = "kitty"
    backup_term = "urxvt"


@dataclass
class Options:
    keys = KeyOptions()
    paths = Paths()
