from __future__ import absolute_import, division, print_function
from dotenv import Dotenv
from os.path import join, dirname
import os
import socket
import sys

dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env")) # Of course, replace by your correct path
os.environ.update(dotenv)

HUE_BULB_NAME = os.environ.get("HUE_BULB_NAME")
if HUE_BULB_NAME is None:
    print("HUE_BULB_NAME is not set")
    sys.exit(1)

HUE_BRIGE_IP = os.environ.get("HUE_BRIGE_IP")
if HUE_BRIGE_IP is None:
    print("HUE_BRIGE_IP is not set")
    sys.exit(1)

HOMEBRITE_PIN = os.environ.get("HOMEBRITE_PIN")
if HOMEBRITE_PIN is None:
    print("HOMEBRITE_PIN is not set")
    sys.exit(1)

HOMEBRITE_MAC = os.environ.get("HOMEBRITE_MAC")
if HOMEBRITE_MAC is None:
    print("HOMEBRITE_MAC is not set")
    sys.exit(1)

