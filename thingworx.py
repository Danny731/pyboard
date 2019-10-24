import machine, utime, gc
import math
import utime
import machine, network, ubinascii, ujson, urequests, utime,gc

Key = "02f4bab8-a0ec-4366-b02a-11d398f6e2bb"
urlBase = "https://ptcacademic-dev3-twx.es.thingworx.com/Thingworx/"
headers = {"Accept":"application/json","Content-Type":"application/json","AppKey":Key}
def Put(thing, property, type, value):
     urlValue = urlBase + 'Things/' + thing + '/Properties/*'
     propValue = {property:value}
     #  assume that the tag is already created  -      urequests.put(urlTag,headers=headers,json=propName).text
     try:
          response = urequests.put(urlValue,headers=headers,json=propValue)
          print(response.text)
          response.close()
     except:
          print('error')

Put('Thing~Spike', 'test', 'NUMBER',668)
