from __future__ import absolute_import, division, print_function
import argparse
import csrmesh as cm
from time import sleep
from phue import Bridge
from settings import *
import traceback


def read_bulb_state():
    state = None
    try:
        b = Bridge(HUE_BRIGE_IP)

        # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
        b.connect()

        bulb_state = b.get_light(HUE_BULB_NAME)
        if 'name' in bulb_state:
            print(bulb_state['state']['on'])
            print(bulb_state['state']['bri'])
            state = bulb_state['state']
        else:
            print("Error reading bulb state: ", bulb_state[0]['error'])
    except Exception as e:
        s = traceback.format_exc()
        print("unexpected failure, {} ,{}".format(e, s))

    return state


def set_homebrite_bulb(level):
    cm.lightbulb.set_light(HOMEBRITE_MAC, HOMEBRITE_PIN, level, 255, 255, 255, 0)

if __name__ == "__main__":
    while True:
        state = read_bulb_state()
        print(state)
        if (state is not None):
            if state['on']:
                level = state['bri']
            else:
                level = 0
            print("Setting level to ", level)
            set_homebrite_bulb(level)
        sleep(0.5)