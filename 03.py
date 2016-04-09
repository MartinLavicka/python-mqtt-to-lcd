#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lcddriver
import time
import datetime
import paho.mqtt.client as mqtt

lcd = lcddriver.lcd()
      lcd.lcd_display_string("                ", 1)
      lcd.lcd_display_string("                ", 2)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic)
    lcd.lcd_display_string("Topic: "+msg.topic, 1)
    print(str(msg.payload))
    lcd.lcd_display_string("Message: "+str(msg.payload), 2)

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