#!/usr/bin/env bash

# TODO: detect Darwin/Mac

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
if [ "$distro" == "Ubuntu" ]; then
    sudo apt update
    sudo apt install git python3-pip -y
    sudo cp keyboard /etc/default/keyboard
elif [[ $distroname == "Arch" ]]; then
    sudo pacman -Syy
    sudo pacman -S git python-pip
fi

#install homely
pip install homely --user

#start up homely and sync
homely update
