#!/usr/bin/env python3

import paho.mqtt.publish as publish
import sys

def POST():
	if len(sys.argv) != 3:
		print("Usage: "+sys.argv[0]+" <ip> <message>")
	else:
		publish.single("temp", str(sys.argv[2]), hostname=str(sys.argv[1]))

POST()