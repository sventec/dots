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

### zsh

The zsh config provided here requires some minimal prerequisite setup. It uses the [antidote](https://github.com/mattmc3/antidote) plugin manager, which will be automatically bootstrapped if not present on the system.

#### Prerequisites

There are tool hooks that expect the following to be installed. Comment or remove these if not needed:

- [pnpm](https://pnpm.io/) - Node package manager
- [nvm](https://github.com/nvm-sh/nvm) - Node version manager
- [keychain](https://www.funtoo.org/Funtoo:Keychain) - SSH keychain management
- [pyenv](https://github.com/pyenv/pyenv) - Python version manager
- [cargo](https://doc.rust-lang.org/cargo/) - Rust package manager
- [zoxide](https://github.com/ajeetdsouza/zoxide) - Directory switching

#### `.zshenv`

Copy the `.zshenv.example` file to `~/.zshenv`, and edit the placeholder variables. All variables in this file are
currently optional, and enable additional functionality for [nvim](#neovim), [qtile](#qtile), and [zsh](#zsh). For nvim
and zsh, it enables [Code::Stats](https://codestats.net/) integration, and for qtile it allows for use of the weather
and [OpenWeather](https://openweathermap.org/api) widgets.

#### Read before using

If adopting this config for your own use, there are likely a number of commands and aliases that will be nonfunctional
and/or useless for you. Consider reading the dotfiles and removing these. For example, `ls` is aliased to
[`eza`](https://github.com/eza-community/eza). If you don't have `eza` installed, be sure to change this before applying
this config. The same applies to the prerequisites above, etc.

### Others

- Terminal emulator: [kitty](./.config/kitty/kitty.conf) ([homepage](https://sw.kovidgoyal.net/kitty/))
- Git client: [lazygit](./.config/lazygit/config.yml) ([homepage](https://github.com/jesseduffield/lazygit))
- Firefox vim motions: [tridactyl](./.tridactylrc) ([homepage](https://github.com/tridactyl/tridactyl))

## TODO

- Add dotfiles for
  - [x] kitty
  - [ ] qtile
  - [x] zsh
    - [x] p10k
    - [x] .zshrc
    - [x] antidote zsh_plugins.txt
    - [x] example .zshenv?
  - [x] ruff
  - [x] tmux
  - [x] lazygit
  - [ ] zellij(?)
