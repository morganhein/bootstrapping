#!/usr/bin/env bash

# TODO: detect Darwin/Mac

echo "You kick ass. Remember to update this as you make changes!\n\n"
arch=$(uname -m)
kernel=$(uname -r)
if [ -n "$(command -v lsb_release)" ]; then
	distroname=$(lsb_release -s -d)
elif [ -f "/etc/os-release" ]; then
	distroname=$(grep PRETTY_NAME /etc/os-release | sed 's/PRETTY_NAME=//g' | tr -d '="')
elif [ -f "/etc/debian_version" ]; then
	distroname="Debian $(cat /etc/debian_version)"
elif [ -f "/etc/redhat-release" ]; then
	distroname=$(cat /etc/redhat-release)
else
	distroname="$(uname -s) $(uname -r)"
fi

distro=""
if [[ $distroname =~ "Ubuntu" ]]; then
    distro="Ubuntu"
elif [[ $distroname =~ "Arch" ]]; then
    distro="Arch"
# Need to decide on what Yum/Dnf based distro to use
# elif [[ $distroname =~ "Cent" ]]; then
#     distro="Centos"
elif [[ $distroname =~ "Alpine" ]]; then
    distro="Alpine"
fi

#todo: detect if distro is empty and just quit

echo "Detected distroname: ${distroname}
Distro is set to: ${distro}"

#update package manager
#install git
#install pip
# https://pip.pypa.io/en/stable/user_guide/#running-pip
PIP="pip"
if [ "$distro" == "Ubuntu" ]; then
    sudo apt update
    sudo apt install git python3-pip -y
    #git clone git@github.com:morganhein/bootstrapping.git /tmp/bootstrapping
    #sudo cp /tmp/bootstrapping/keyboard /etc/default/keyboard
    PIP="/usr/bin/pip3"
    #TODO: Add this to bashrc?
    export PATH="$PATH:$HOME/.local/bin:$(python3 -m site --user-site)"
elif [[ $distroname == "Arch" ]]; then
    sudo pacman -Syu
    sudo pacman -S git python3-pip
fi

#install homely
${PIP} install homely --user --no-binary :all:

#start up homely and sync
homely add https://github.com/morganhein/bootstrapping.git $HOME/.local/homely
homely update
