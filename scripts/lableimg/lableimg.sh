#!/bin/bash
#Functions are run twice to catch any errors

function check_root
{
if [ "$EUID" -ne 0 ];then
    echo "Please run script with sudo"
  exit
fi
}

function check_internet
{
echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Please make sure you're connected to the internet"
    exit
fi
}

check_root
check_internet
apt install git pyqt5-dev-tools python3-lxml python3-pyqt5
su - "$SUDO_USER" -c "git clone https://github.com/tzutalin/labelImg.git"
su - "$SUDO_USER" -c "make qt5py3 -C ~/labelImg"

