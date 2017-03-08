This code enables Philips HUE to control Feit Electric HomeBrite Smart LED bulbs (and perhaps other CSRmesh-based
equipment). This is done by have a Raspberry Pi monitor the state of an existing Philips HUE lightbulb and then using
BLE to set the brightness level of a HomeBrite bulb.

In fact, this code uses th broadcast option to change the brightness level of your entire mesh. If you want to control
individual bulbs, feel free to change the code :)

Note - this code uses the [csrmesh python library](https://github.com/nkaminski/csrmesh) created by Nash Kaminski.
Thanks Nash!

# Setting up HUE and HomeBrite
This part is straightforward - setup your HUE and HomeBrite systems as usual. Make sure your write down the PIN used
 for configuring the HomeBrite Bulbs.

# Finding the MAC address of a HomeBrite bulb
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

If the script fails to connect to the bulb, make sure you exit the HomeBrite app, and perhaps even restart your phone.
It seems that the app keeps an open connection to the bulb (sometimes?), and therefore blocks other connections.

# Optional - loading code on boot with supervisor
If you want the bridge code to start when the RasPi boots, you can use supervisor:

* Install supervisor: sudo apt-get install supervisor
* Create a config file: sudo touch /etc/supervisor/conf.d/csrmesh-hue-bridge.conf
* Edit the file and add the following lines:
```
[program:bridge]
command=python /home/pi/csrmesh-hue-bridge/csrmesh-hue-bridge.py
directory=/home/pi/csrmesh-hue-bridge/
autostart=true
autorestart=unexpected
```
* Ask supervisor to start new services: sudo supervisorctl reread && sudo supervisorctl update
* Make sure the process is up: sudo supervisorctl status
```
bridge                           RUNNING    pid 5168, uptime 0:01:36
```
