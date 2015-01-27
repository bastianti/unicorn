#!/usr/bin/env python

import unicornhat as UH
import time
import colorsys

UH.brightness(1)
r = 255
g = 0
b = 0
h = 0.002
s = 0.76
v = 1

while True:
    h = h+0.001
    rgb = colorsys.hsv_to_rgb(h,s,v)
    print h,s,v
    print int(rgb[0]*254),
    print int(rgb[1]*254),
    print int(rgb[2]*254)
    for y in range(8):
      for x in range(8):
        r = int(rgb[0]*120)
        g = int(rgb[1]*120)
        b = int(rgb[2]*120)
        UH.set_pixel(x,y,r,g,b)
#    time.sleep(0.1)
        #print "UH.set_pixel({0},{1},{2},{3},{4})".format(x,y,r,g,b)
    UH.show() 
