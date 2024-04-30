# Public dotfiles

Public mirror of select (stable) configs from my personal dotfiles.

## Available configs

### Neovim

For my Neovim config, see [this dedicated repo](https://github.com/sventec/nvim).

### Ruff

Ever-changing default configuration for [ruff](https://docs.astral.sh/ruff/).
If there are no project-specific config sections for ruff, it will fall back to
`~/.config/ruff/pyproject.toml`, thus the existence of this file. The version
included here is **very** verbose, you will likely not want to
use it as-is. Instead, use it as a baseline to help determine which rules are
helpful, and which you feel are superfluous.

### Tmux

I have also been experimenting with [`zellij`](https://zellij.dev/), but still use `tmux` more frequently.

This config requires [tpm](https://github.com/tmux-plugins/tpm#installation) for plugin management:

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

### Others

- Terminal emulator: [kitty](./kitty/kitty.conf) ([homepage](https://sw.kovidgoyal.net/kitty/))

## TODO

- Add dotfiles for
  - [x] kitty
  - [ ] qtile
  - [ ] zsh
    - [ ] p10k
    - [ ] .zshrc
    - [ ] antidote zsh_plugins.txt
    - [ ] example .zshenv?
  - [x] ruff
  - [x] tmux
  - [ ] zellij(?)
