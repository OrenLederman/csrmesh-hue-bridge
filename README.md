This code enables Philips HUE to control Feit Electric HomeBrite Smart LED bulbs (and perhaps other CSRmesh-based
equipment). This is done by have a Raspberry Pi monitor the state of an existing Philips HUE lightbulb and then using
BLE to set the brightness level of a HomeBrite bulb.

Note - this code uses the [csrmesh python library](https://github.com/nkaminski/csrmesh) created by Nash Kaminski.
Thanks Nash!

# Setting up HUE and HomeBrite
This part is straightforward - setup your HUE and HomeBrite systems as usual. Make sure your write down the PIN used
 for configuring the HomeBrite Bulbs.

# Finding the MAC address of your HomeBrite bulb
In order to connect to the HoemBrite mesh, you need to know the MAc address of one of the bulbs. To do that, either use
a phone app (I recommend [nRF Connect](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp) or the
hcitool lescan command(see below). Look for a device called "Feit Bulb".

```
> sudo hcitool lescan
LE Scan ...
79:24:AD:C9:68:68 (unknown)
79:24:AD:C9:68:68 (unknown)
80:E4:DA:70:3A:CE f008cDrO
80:E4:DA:70:3A:CE (unknown)
00:00:C1:00:D9:A8 Feit Bulb
00:00:C1:00:D9:A8 (unknown)
```

Note - sometimes the bulb won't show up in the scan. I found that it is sometimes easier to find it right after powering
up the bulb.

# Installation
1. Install python 2.7 (it you haven't already)
2. Install required libraries: sudo apt-get install python-dev python-pip git
3. Clone this repository: git clone https://github.com/OrenLederman/csrmesh-hue-bridge.git
4. cd csrmesh-hue-bridge
5. Install python dependencies: sudo pip install -r requirements.txt
6. Create a .env file and setup the bulb name, PIN code, etc. You can use the env_template file as reference
7. Try it out - python csrmesh-hue-bridge.py . Important! The first time you try it, you will need to press the button
on the HUE Bridge to register your Raspberry Pi

# Optional - supervisord
TBD
sudo apt-get install supervisor
/etc/supervisor/conf.d/csrmesh-hue-bridge.conf
supervisorctl reread
