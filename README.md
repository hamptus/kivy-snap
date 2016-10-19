# kivy-snap
An attempt to get kivy working as a snap

## The problem

With Kivy properly installed on Ubuntu, calling python main.py works. Typing text into the TextInput shows text and prints the event to the console. When running the code as a snap the event gets printed to the console, but nothing appears in the TextInput widget.

## How to replicate

1. Install snapd: http://snapcraft.io/docs/core/install
2. Clone this project: `git clone git@github.com:hamptus/kivy-snap.git`
3. Change to the new directory: `cd kivy-snap`
4. Build the snap by entering: `snapcraft`
5. Install the snap (this is for Ubuntu, it may differ for other distros): `sudo snap install kivysnap*.snap --force-dangerous --devmode`
6. Run the snap by entering: `kivysnap`
7. Type into the TextInput

If you want to modify the `snapcraft.yaml`, just run `snapcraft clean` before running `snapcraft` again.

The command I usually run to build, install, then run the command is:

`snapcraft clean && snapcraft && sudo snap install kivysnap*.snap --force-dangerous --devmode && kivysnap`