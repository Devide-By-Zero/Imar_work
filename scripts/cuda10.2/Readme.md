# Cuda 10.2 Setup Script

## Introduction


This script is for autonomously doing most of the setup for Cuda 10.2

  

## What It Does

1. This script will check if gcc is installed [Requirement for cuda] 
if not it will automatically install it

2. Next it will create a modprobe config. Disabling nouveau on next boot

3. Finally it will download the Nvidia and Cuda Driver and make it executable

## After Setup Instructions

After this is done the PC Needs to be restarted and when grub loads showing boot options press 'e' (shown in figure below)

![Grub BootLoader](https://www.howtogeek.com/wp-content/uploads/2014/09/gnu-grub2-boot-loader-menu.png?trim=1,1&bg-color=000&pad=1,1)

  

After this you can edit boot commands

Find the line starting with Linux and type a '3' at the end

![Grub Command Editor](https://documentation.suse.com/sles/15-SP2/single-html/SLES-admin/images/grub2_edit_config.png)
Press F10 to boot into Runlevel 3

After this, Login and navigate to the Downloads folder
```bash
cd ~/Downloads
```
Start the Run file
```bash
sudo ./cuda_10.2.89_440.33.01_linux.run
```
Type accept

![Nvidia EUAL](https://actruce.com/wp-content/uploads/2021/04/runfile02.png)

  

Here I recommend pressing 'a' over driver and checking "Update the system X config file" using the arrow keys and enter

![Nvidia installer](https://actruce.com/wp-content/uploads/2021/04/runfile03.png)

Then press install and wait...

Next read the summary as you may need to add lines to .bashrc similar to these

```bash
export PATH=<cuda install location>/cuda-10.2/bin${PATH:+:${PATH}}

#for 64bit os
export LD_LIBRARY_PATH=<cuda install location>/cuda-10.2/lib64\
${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

#for 32bit os
export LD_LIBRARY_PATH=<cuda install location>/cuda-10.2/lib\
${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
 Finally reboot normally and Nvidia X-Org server should take over.
This can be checked using
```bash
#driver
nvidia-smi
#cuda
nvcc --version
