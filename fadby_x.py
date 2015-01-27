#!/usr/bin/env python

import unicornhat as UH
import time
import colorsys
import math

UH.brightness(0.7)
r = 255
g = 0
b = 0
h = 0.002
s = 0.76
v = 1
sleep = 0.5

while True:
    for x in range(0,7,1):
      h = h+0.142857142857
      rgb = colorsys.hsv_to_rgb(h,s,v)
      print h,s,v
      print int(rgb[0]*254),
      print int(rgb[1]*254),
      print int(rgb[2]*254)
      for y in range(8):
        r = int(rgb[0]*120)
        g = int(rgb[1]*120)
        b = int(rgb[2]*120)
        UH.set_pixel(x,y,r,g,b)
        #print "UH.set_pixel({0},{1},{2},{3},{4})".format(x,y,r,g,b)
      UH.show() 
      time.sleep(sleep)
      #UH.clear()  
    for x in range(7,0,-1):
      rgb = colorsys.hsv_to_rgb(h,s,v)
      print h,s,v
      for y in range(7,-1,-1):
        r = int(rgb[0]*120)
        g = int(rgb[1]*120)
        b = int(rgb[2]*120)
        UH.set_pixel(x,y,r,g,b)
        print x
        if x > 6:
          x = 6
      for y in range(7,-1,-1):
        rgb = colorsys.hsv_to_rgb(h,s,v-0.5)
        r = int(rgb[0]*120)
        g = int(rgb[1]*120)
        b = int(rgb[2]*120)
        UH.set_pixel(x+1,y,r,g,b)
      time.sleep(sleep)
      UH.show() 
      for y in range(7,-1,-1):
        rgb = colorsys.hsv_to_rgb(h,s,v)
        r = int(rgb[0]*120)
        g = int(rgb[1]*120)
        b = int(rgb[2]*120)
        UH.set_pixel(x+1,y,r,g,b)
      UH.show() 
      h = h-0.142857142857
      #UH.clear()  
