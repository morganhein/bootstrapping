# ~/bootstrapping/HOMELY.py

# TODO: add pacman/arch linux support to homely
# TODO: add a command to homely to update the package manager
# TODO: add a command to homely to run command as sudo

from homely.files import mkdir
from homely.install import installpkg
from homely.files import symlink
from homely.system import execute, haveexecutable
# create ~/.config first - mkdir() is not recursive
# NOTE that we use homely's mkdir() not os.mkdir()
mkdir('~/.config/git')
mkdir('~/.config')

# symlink git
symlink('git/config', '~/.config/git/config')
symlink('git/ignore', '~/.config/git/ignore')
#bashrc profiles
#should we somehow instead *add* to the bashrc instead?
symlink(' .bashrc', '~/.bashrc')

#install zsh https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH
installpkg('zsh', apt='zsh', apk='zsh', pac='zsh', brew='zsh')

if haveexecutable('curl') and haveexecutable('sh'):
    execute(['sh', '-c', '"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"])

# TODO: install powerline into zsh

# install fish https://fishshell.com/
if haveexecutable('apt'):
    execute(['sudo', 'apt-add-repository', 'ppa:fish-shell/release-3'])
    execute(['sudo', 'apt', 'update'])
     
installpkg('fish', apt='fish', apk='fish', pac='fish', brew='fish')

# TODO: things to install
# autojump

#install fd https://github.com/sharkdp/fd
installpkg('fd', apt='fd-find', apk='fd', pac='fd', brew='fd')
#install bat https://github.com/sharkdp/bat
installpkg('bat', apt='bat', apk='bat', pac='bat', brew='bat')

# TODO: Detect if in interactive session, and request if we want these installed:
#install goup/gvm, set default go version
#curl -sSf https://raw.githubusercontent.com/owenthereal/goup/master/install.sh | sh -s -- '--skip-prompt'
#node/npm
#ssh agent / my ssh key
#1password cli maybe?