#!/usr/bin/env python3

import paho.mqtt.publish as publish
import sys

def POST():
	if len(sys.argv) != 3:
		print("Usage: "+sys.argv[0]+" <ip> <topic> <message>")
	else:
		publish.single(str(sys.argv[2], str(sys.argv[3]), hostname=str(sys.argv[1]))

POST()
