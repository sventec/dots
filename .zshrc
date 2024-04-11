# .zshrc zsh config

# Enable Powerlevel10k instant prompt.
# ------------------------------------
# Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
    source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Clone antidote (plugin manager) if necessary.
# ---------------------------------------------
[[ -e $HOME/.antidote ]] ||
git clone --depth=1 https://github.com/mattmc3/antidote.git $HOME/.antidote

# === zsh options ===
setopt correct           # Auto-correct mistakes
setopt extendedglob      # Extended globbing. Regex with *
setopt nocaseglob        # Case insensitive globbing
setopt numericglobsort   # Sort filesnames numerically when sane
setopt nobeep            # Don't beep
setopt autocd            # Automatically cd if only dirpath
setopt complete_aliases  # Allow for completion when using aliases

# === path ===
export PATH="$PATH:$HOME/go/bin"
export PATH="$PATH:$HOME/.cargo/bin"
export PATH="$PATH:$HOME/scripts/"
export PATH="$PATH:$HOME/bin"
export PATH="$PATH:$HOME/.npm-global/bin"
# https://github.com/MordechaiHadad/bob
export PATH="$HOME/.local/share/bob/nvim-bin:$PATH"

# === default editors ===
export SHELL="zsh"
export EDITOR="$(which nvim)"
export SUDO_EDITOR="$(which nvim)"
export BROWSER="librewolf"
# export BROWSER="qutebrowser"
export READER="zathura"
export FILE="thunar"

# === aliases ===
# For a full list of active aliases, run `alias`.

# exa replacements for ls
alias ls='exa --color=always --group-directories-first'
alias lsl='exa -la --color=always --group-directories-first --icons'
alias l='exa -la --color=always --group-directories-first --icons'
alias lsd='lsd --group-dirs first --color always'
alias lsla='exa --long --header --git --all'
alias lsr='exa -lr --sort=mod --color=always'
alias lsra='exa -lra --sort=mod --color=always'
alias lstree='exa -T'

# shortcuts
alias cp='cp -v'
alias chx='chmod +x'
alias gi='grep -i'
alias ra='ranger'
alias nb='newsboat'
alias lg='lazygit'
alias ze='zellij'
alias loc='plocate'
alias mvp="mkdir -vp" # Verbose mkdir
alias tns="tmux new -s" # New tmux session. Usage: tns NAME_OF_SESSION
alias cl="clear" # Shorter window clearing, also <C-l>
alias e="exit" # Shorter shell exiting
alias v="nvim"
alias za="zathura"
alias copy="xsel -ib"

# python aliases
alias py="python3"
alias pdmvenv='eval "$(pdm venv activate)"'
alias activate='. .venv/bin/activate'  # `deactivate` built-in
alias uvfreeze="uv pip freeze | uv pip compile - -o requirements.txt"

# shortcuts with fill/completion
alias se='nvim $(fzf --reverse --height 40%)'
alias newnote='nvim $(date -I).md'
# (modified from fzf ArchWiki page):
alias pkgsearch="yay -Slq | fzf --multi --preview 'yay -Si {1}' | xargs -ro yay -S"

# subcommand shortcuts
alias psforest='ps -aef --forest'
alias timeoutoff='xset s off'
alias timeouton='xset s 300'
alias wgup='sudo wg-quick up'
alias wgdown='sudo wg-quick down'
alias listkeys='gpg --list-secret-keys --keyid-format=long'
alias fontupdate="fc-cache -fv"

# etc
alias zshsrc="source ~/.zshrc"
alias drun="rofi -modi drun -show drun"
alias wttr="curl wttr.in/$WTTR_LOCATION" # e.g. "New_York"
alias wttrv2="curl v2.wttr.in/$WTTR_LOCATION"
# spotifyd
alias startspotify='systemctl --user start spotifyd.service'
alias spotifydnd='spotifyd --no-daemon'
# wolfram alpha
alias wa="$HOME/scripts/wa"

# === plugin/program options ===
# fzf

export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git --exclude .cargo --exclude .cache'
# export FZF_COMPLETION_TRIGGER='~~'

# set QT5 theme
export QT_STYLE_OVERRIDE=kvantum

# zsh vi mode config
function zvm_config() {
    ZVM_LINE_INIT_MODE=$ZVM_MODE_INSERT
    ZVM_READKEY_ENGINE=$ZVM_READKEY_ENGINE_NEX
}
# Source zish-vi-mode in normal plugin order
# Fixes overwriting fzf <C-r> keybind
export ZVM_INIT_MODE=sourcing

# You Should Know (alias tips)
export YSU_MESSAGE_POSITION="before"
export YSU_MODE="BESTMATCH"
export YSU_IGNORED_ALIASES=("_" "ll" "vi" "vim" "nvim")
export YSU_IGNORED_GLOBAL_ALIASES=("..1")

# source antidote (plugin manager)
source ${ZDOTDIR:-~}/.antidote/antidote.zsh
# initialize plugins statically with ${ZDOTDIR:-~}/.zsh_plugins.txt
antidote load

# === functions ===

# color output for dict command
# colorit should ship with dictd
function cdict {
    dict "$1" | colorit
}

# Credit original to Luke Smith
function sc {
    du -a ~/scripts/* ~/.config/* --exclude=coc --exclude=Code --exclude=discord |
    cut -f 2- | fzf --reverse --height 40% | xargs -r $EDITOR
}

function zb {
    du -a ~/school/books/* ~/cloud/books/* |
    cut -f 2- | fzf --reverse --height 40% | xargs -r zathura
}

# multipurpose archive extraction function
# found in DistroTube's dotfiles (gitlab.com/dwt1/dotfiles)
function extract {
    if [ -z "$1" ]; then
        # display usage if no parameters given
        echo "Usage: extract <path/file_name>.<zip|rar|bz2|gz|tar|tbz2|tgz|Z|7z|xz|ex|tar.bz2|tar.gz|tar.xz>"
        echo "       extract <path/file_name_1.ext> [path/file_name_2.ext] [path/file_name_3.ext]"
    else
        for n in "$@"
        do
            if [ -f "$n" ] ; then
                case "${n%,}" in
                    *.cbt|*.tar.bz2|*.tar.gz|*.tar.xz|*.tbz2|*.tgz|*.txz|*.tar)
                        tar xvf "$n"       ;;
                    *.lzma)      unlzma ./"$n"      ;;
                    *.bz2)       bunzip2 ./"$n"     ;;
                    *.cbr|*.rar)       unrar x -ad ./"$n" ;;
                    *.gz)        gunzip ./"$n"      ;;
                    *.cbz|*.epub|*.zip)       unzip ./"$n"       ;;
                    *.z)         uncompress ./"$n"  ;;
                    *.7z|*.arj|*.cab|*.cb7|*.chm|*.deb|*.dmg|*.iso|*.lzh|*.msi|*.pkg|*.rpm|*.udf|*.wim|*.xar)
                        7z x ./"$n"        ;;
                    *.xz)        unxz ./"$n"        ;;
                    *.exe)       cabextract ./"$n"  ;;
                    *.cpio)      cpio -id < ./"$n"  ;;
                    *.cba|*.ace)      unace x ./"$n"      ;;
                    *)
                        echo "extract: '$n' - unknown archive method"
                        return 1
                        ;;
                esac
            else
                echo "'$n' - file does not exist"
                return 1
            fi
        done
    fi
}

# source optional fzf settings
# needed when installed via pacman
# paths can be distro specific
source /usr/share/fzf/key-bindings.zsh
source /usr/share/fzf/completion.zsh

# === tool setups ===

# pnpm
export PNPM_HOME="/home/fx/.local/share/pnpm"
export PATH="$PNPM_HOME:$PATH"

# nvm (node version management)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# ssh-agent type functionality for remembering ssh key password
# requires `keychain`
eval "$(keychain --noask -q --eval id_rsa)"

# pyenv (python version management)
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# cargo env
. "$HOME/.cargo/env"

# init zoxide (installed via install script)
eval "$(zoxide init zsh)"

# p10k end setup
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
