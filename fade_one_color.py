#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicornhat as UH
import time
import colorsys
from random import randint

UH.brightness(1)
r = 255
g = 0
b = 0
h = float(0/50) # Farbwert als Farbwinkel H auf dem Farbkreis (etwa 0 für Rot, 120 für Gruen, 240 für Blau)
s = 1 # Sättigung S in Prozent (0 % = Neutralgrau, 50 % = wenig gesättigte Farbe, 100 % = gesättigte, reine Farbe) oder in einem Intervall von Null bis Eins
v = 0 # Hellwert V als Prozentsatz (0 % = keine Helligkeit, 100 % = volle Helligkeit), oder in einem Intervall von Null bis Eins, auch Dunkelstufe genannt.
step = 0.01

while True:
    v = v+step
    rgb = colorsys.hsv_to_rgb(h,s,v)
#    print h,s,v
 #   print int(rgb[0]*120),
 #   print int(rgb[1]*120),
 #   print int(rgb[2]*120)
    for y in range(8):
      for x in range(8):
        r = int(rgb[0]*120)
        g = int(rgb[1]*120)
        b = int(rgb[2]*120)
        UH.set_pixel(x,y,r,g,b)
    #time.sleep(0.1)
    print v
        #print "UH.set_pixel({0},{1},{2},{3},{4})".format(x,y,r,g,b)
    UH.show() 
    if v > 2.12:
      while True:
        v = v-step
        print v
        rgb = colorsys.hsv_to_rgb(h,s,v)
 #       print h,s,v
 #       print int(rgb[0]*120),
 #       print int(rgb[1]*120),
 #       print int(rgb[2]*120)
        for y in range(8):
          for x in range(8):
            r = int(rgb[0]*120)
            g = int(rgb[1]*120)
            b = int(rgb[2]*120)
            UH.set_pixel(x,y,r,g,b)
        UH.show()
       # time.sleep(0.1)
        print v
        if v < 0.050:
          break
        #print "UH.set_pixel({0},{1},{2},{3},{4})".format(x,y,r,g,b)

