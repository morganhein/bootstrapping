# ~/bootstrapping/HOMELY.py

# TODO: add pacman/arch linux support to homely
# TODO: ability to symlink using sudo
# TODO: add a command to homely to update the package manager
# TODO: add a command to homely to run command as sudo
# TODO: things to install
    # autojump
    # powerline into zsh
    # install norman layout

from homely.files import mkdir, download
from homely.install import installpkg
from homely.files import symlink
from homely.system import execute, haveexecutable
from homely.ui import yesno

#create ~/.config first - mkdir() is not recursive
#NOTE that we use homely's mkdir() not os.mkdir()
mkdir('~/.config/git')
mkdir('~/.config')

#symlink git
symlink('git/config', '~/.config/git/config')
symlink('git/ignore', '~/.config/git/ignore')
#link aliases
symlink('bash/.aliases', '~/.aliases')

if yesno("install_norman", "install the norman layout?", default=True):
#     #TODO: need to handle mac
    execute(["sudo", "cp", "/etc/default/keyboard", "/etc/default/keyboard.bak"])
    execute(['sudo','sed', '-i',r's/XKBVARIANT=\"\w*"/XKBVARIANT=\"norman\"/g','/etc/default/keyboard'])

#install zsh https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH
installpkg('zsh', apt='zsh', pacman='zsh', brew='zsh')

#install oh-my-zsh
if haveexecutable('curl') and haveexecutable('sh'):
    mkdir('/tmp/oh-my-zsh')
    download('https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh', '/tmp/oh-my-zsh/install.sh')
    execute(['chmod', '+x', '/tmp/oh-my-zsh/install.sh'])
    #execute(['sh', '-c', '/tmp/oh-my-zsh/install.sh'])

# install fish https://fishshell.com/
if haveexecutable('apt'):
    execute(['sudo', 'apt-add-repository', 'ppa:fish-shell/release-3'])
    execute(['sudo', 'apt', 'update'])
     
installpkg('fish', apt='fish', pacman='fish', brew='fish')

#install fd https://github.com/sharkdp/fd
installpkg('fd', apt='fd-find', pacman='fd', brew='fd')
#install bat https://github.com/sharkdp/bat
installpkg('bat', apt='bat', pacman='bat', brew='bat')

#Sets up the SSH folder with correct permissions
#https://superuser.com/a/1559867
if yesno("configure_ssh", "configure ssh?", default=True, recommended=True):
    mkdir("$HOME/.ssh")
    execute(['chmod', '700', '$HOME/.ssh'])
    execute(['touch', '$HOME/.ssh/authorize_keys'])
    execute(['chmod', '644', '$HOME/.ssh/authorized_keys'])
    execute(['chmod', '600', '$HOME/.ssh/id*'])

if yesno("install_1pass", "install 1password cli?", default=True, recommended=True):
    #if this is linux, we need gpg and unzip.
    installpkg('gpg', apt='gpg', pacman='gpg', brew='gpg')
    installpkg('unzip', apt='unzip', pacman='unzip', brew='unzip')
    execute(['bash', 'apps/1password.sh'])
    if yesno("install_ssh_key", "install ssh key?", default=False, recommended=True):
        # TODO: perform SSH key download tasks
        print("THIS AIN'T DONE YET") 


if yesno("install_goup", "install go version manager (goup?)", default=False, recommended=False):
    download('https://raw.githubusercontent.com/owenthereal/goup/master/install.sh', '/tmp/goup-install.sh')
    execute(['chmod', '+x', '/tmp/goup-install.sh'])
    execute(['sh', '/tmp/goup-install.sh', '--skip-prompt'])
    
# TODO: Detect if in interactive session, and request if we want these installed:
#install goup/gvm, set default go version
#curl -sSf https://raw.githubusercontent.com/owenthereal/goup/master/install.sh | sh -s -- '--skip-prompt'
#node/npm