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
        print("Connectin established! rcode("+str(rc)+")")
        client.subscribe("temp")


def on_message(client, userdata, msg):
    print(msg.payload.decode("utf-8"))
    target = open("temp.dat", 'w')
    target.write(msg.payload.decode("utf-8"))
    target.close()


def main():
    if len(sys.argv) != 2:
        print("Usage: "+sys.argv[0]+" <ip>")
    else:
        try:
            start_broker()
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect(str(sys.argv[1]), 1883, 60)
            client.publish("temp", "online")
            client.loop_forever()
        except KeyboardInterrupt:
            stop_broker()


if __name__ == '__main__':
    main()
