#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import sys
import os


def start_broker():
    print("Starting mqtt broker...")
    os.system('mosquitto -d')


def stop_broker():
    print("\nStopping mqtt broker")
    os.system("killall 'mosquitto'")


def on_connect(client, userdata, flags, rc):
    if(rc == 0):
        print("Connecting established! rcode("+str(rc)+")")
        for topics in sys.argv[2].split(", "):
            print("Subscribed to "+topics)
            client.subscribe(topics)


def on_message(client, userdata, msg):
    print(msg.topic+": \""+msg.payload.decode("utf-8").replace(" ", "")+"\"")


def main():
    if len(sys.argv) != 3:
        print("Usage: "+sys.argv[0]+" <ip> <topics>")
    else:
        try:
            start_broker()
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect(str(sys.argv[1]), 1883, 60)
            client.loop_forever()
        except KeyboardInterrupt:
            stop_broker()


if __name__ == '__main__':
    main()
