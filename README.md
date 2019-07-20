# LED-Games

 Python code for playing games on a custom build 11x11 led matrix with retro gamepads. 
 
 ## Setup
 
You have to install the packages `evdev` and  `aiostream`. Be aware that installing `evdev` requires some dependencies from your system, that are a bit cumbersome to set up within an anaconda environment.

**Debian based:**

```bash
apt-get install python-dev python-pip gcc
apt-get install linux-headers-$(uname -r)

```
**Redhat based:**

```bash
yum install python-devel python-pip gcc
yum install kernel-headers-$(uname -r)
```

**Arch based:**

```bash
pacman -S core/linux-api-headers python-pip gcc
```

**Note:** In Arch you don't have to install any \*-dev packages as Arch already ships the header files with the normal packages.

Now the required packages should be installable.

```bash
pip install evdev aiostream
```

## Miscellaneous

This project is in a very early stage and some convenience features, like other gamepads or handling of disconnected gamepads, might be added either later or never.
