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

function test_curl
{
curl_installed=false
curl=$(apt list --installed curl 2>/dev/null | grep curl)
    if [ -n "$curl" ]; then
        curl_installed=true
    else
        apt install -y curl 2>/dev/null
    fi
}

function test_ROS_Melodic
{
ROS_installed=false
ROS=$(apt list --installed ros-melodic-desktop-full 2>/dev/null | grep ros-melodic-desktop-full)
    if [ -n "$ROS" ]; then
        ROS_installed=true
    else
        apt install -y ros-melodic-desktop-full 2>/dev/null
    fi
}

function test_ROS_Tools
{
ROS_Tools_installed=false
ROS_Tools=$(apt list --installed python-rosdep 2>/dev/null | grep python-rosdep)
    if [ -n "$ROS_Tools" ]; then
        ROS_Tools_installed=true
    else
        apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential 2>/dev/null
    fi
}
check_root
check_internet
echo "Adding ros packages to source list"
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
test_curl
test_curl
if [ "$curl_installed" = true ]; then
    echo "curl installed"
    echo "Adding ros keys"
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
    apt update
    test_ROS_Melodic
    test_ROS_Melodic
    if [ "$ROS_installed" = true ]; then
      bashrc_append=$(su - "$SUDO_USER" -c "cat ~/.bashrc | grep /opt/ros/melodic/setup.bash")
      if [ -z "$bashrc_append" ]; then
        echo "Adding ros to bashrc"
        su - "$SUDO_USER" -c "echo 'source /opt/ros/melodic/setup.bash' >> ~/.bashrc"
      fi
        echo "reloading bashrc"
        su - "$SUDO_USER" -c "source ~/.bashrc"
        test_ROS_Tools
        test_ROS_Tools
        if [ "$ROS_Tools_installed" = true ]; then
          echo "ROS Tools are installed"
          rosdep init
          su - "$SUDO_USER" -c "rosdep update"
          echo "Install completed"
        else
          echo "Make sure you are connected to the internet"
          exit
        fi
    else
      echo "Make sure you are connected to the internet"
      exit
    fi
else
    echo "Make sure you are connected to the internet"
    exit
fi