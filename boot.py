# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()

import esp
esp.osdebug(None)

def connect():
 import network
 import time
 ssid = 'Tufts_Wireless'    # insert your WiFi ssid here
 password = ''     # insert your WiFi pass here
 # Create Station interface
 sta_if = network.WLAN(network.STA_IF) 
 if not sta_if.isconnected():
  print('Connecting to',ssid,'...')
  # Enable the interface
  sta_if.active(True)
  # Connect
  sta_if.connect(ssid, password)
  # Wait till connection is established
  while not sta_if.isconnected():
   time.sleep_ms(300)
  print('Your device is now connected.')
 else:
  print('Already Connected.')   
  print('Network Settings:', sta_if.ifconfig())

connect()
