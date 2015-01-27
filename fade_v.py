#!/usr/bin/env python

import unicornhat as UH
import time
import colorsys
from random import randint

UH.brightness(0.7)
h = 0
s = 0
v = 1
step = 0.01
while True:
    s = s+step
    rgb = colorsys.hsv_to_rgb(h,s,v)
    print h,s,v
 #   print int(rgb[0]*120),
 #   print int(rgb[1]*120),
 #   print int(rgb[2]*120)
    for y in range(8):
      for x in range(8):
        r = int(rgb[0]*255)
        g = int(rgb[1]*255)
        b = int(rgb[2]*255)
        UH.set_pixel(x,y,r,g,b)
    #time.sleep(0.1)
    print s
    print "UH.set_pixel({0},{1},{2},{3},{4})".format(x,y,r,g,b)
    UH.show() 
    if s > 0.9:
      while True:
        s = s-step
        print s
        rgb = colorsys.hsv_to_rgb(h,s,v)
 #       print h,s,v
 #       print int(rgb[0]*120),
 #       print int(rgb[1]*120),
 #       print int(rgb[2]*120)
        for y in range(8):
          for x in range(8):
            r = int(rgb[0]*255)
            g = int(rgb[1]*255)
            b = int(rgb[2]*255)
            UH.set_pixel(x,y,r,g,b)
        UH.show()
       # time.sleep(0.1)
        if s < 0.050:
          break
        #print "UH.set_pixel({0},{1},{2},{3},{4})".format(x,y,r,g,b)

