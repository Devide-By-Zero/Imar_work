#!/bin/bash
#Functions are run twice to catch any errors

function check_root
{
if [ "$EUID" -ne 0 ];then
    echo "Please run script with sudo"
  exit
fi
}

function test_gcc
{
gcc_installed=false
gcc=$(apt list --installed gcc 2>/dev/null | grep gcc)
    if [ -n "$gcc" ]; then
        gcc_installed=true
    else
        apt install -y gcc linux-headers-$(uname -r) 2>/dev/null
    fi
}

function test_nouveau_modprobe {
FILE=/etc/modprobe.d/nvidia-installer-disable-nouveau.conf
nouveau_modprobe=false
if [ -f "$FILE" ]; then
    nouveau_modprobe=true
else
    echo -e '# generated by script\nblacklist nouveau\noptions nouveau modeset=0' > /etc/modprobe.d/nvidia-installer-disable-nouveau.conf
fi
}

check_root
echo "checking gcc install..."
test_gcc
test_gcc
if [ "$gcc_installed" = true ]; then
    echo "gcc is installed"
    echo "checking nouveau config..."
    test_nouveau_modprobe
    test_nouveau_modprobe
    if [ "$nouveau_modprobe" = true ]; then
        wget -P ~/Downloads https://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_440.33.01_linux.run
        chmod 555 ~/Downloads/cuda_10.2.89_440.33.01_linux.run
        echo -e "\n\nRestart pc and press e at grub\nFind the line starting with linux and add a 3 at the end\npress F10 and log in\nrun the nvidia run file found in home directory"
        exit
    else
        echo "Unable to create modprobe file"
        exit
    fi
else
    echo "Make sure you are connected to the internet"
    exit
fi
