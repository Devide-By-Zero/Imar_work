# ROS 1 Melodic Setup Script

## Introduction

This script is for autonomously installing ROS 1 Melodic.

This is assuming the os is ubuntu 18.04 and the terminal enviroment is bash

## What It Does

1. This script will check for elevated privileges and an internet connection for installing the dependencies and the application 

2. Next it will add the ROS ppa to the repository.

3. Next it will test for an ROS is already installed. if not ROS-melodic-Desktop-Full will be installed

4. Next it will append the ROS enviroment to the bash profile and reload the terminal

5. Next it will install the ROSdep dependencies.

6. Finally it will run ros update to get the enviroment ready 