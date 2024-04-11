# Options referenced in other parts of the configuration
# Values that may be hardware/machine specific, configurable per system, etc.

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Options:
    # Absolute path to qtile config directory
    qtile_path = Path(Path.home() / ".config" / "qtile")

