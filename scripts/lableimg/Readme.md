# labelImg Setup Script

## Introduction


This script is for autonomously installing labelImg

  

## What It Does

1. This script will check for elevated privileges and an internet connection for installing the depenancies and the application 

2. Next it will attempt to install all the required dependancies to run labelImg

3. Next it will clone the git repositiory to the users home directory

4. Finally it will make the application using pyqt5.

## After Setup Instructions

The labelImg folder can be accesed from the home directory

```bash
cd ~/labelImg
```

It can be run from this directory using
```bash
python3 labelImg.py
```