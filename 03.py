#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lcddriver
import time
import datetime
import paho.mqtt.client as mqtt

lcd = lcddriver.lcd()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic)
    print(str(msg.payload))
    lcd = lcddriver.lcd()
    lcd.lcd_display_string("T:"+msg.topic, 1)
    lcd.lcd_display_string("M:"+str(msg.payload), 2)

def main():
  lcd.lcd_clear();
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message

  client.connect("192.168.0.60", 1883, 60)
  client.loop_forever()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd.lcd_clear();