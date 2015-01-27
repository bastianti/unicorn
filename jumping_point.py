#!/usr/bin/env python
import unicornhat as unicorn
import time

unicorn.brightness(0.5)
y = 0
x = 0

while True:
  for x in range(x,8,1):
      y = y + 1
      if y == 8:
        x = x + 1
        for x in range(x,0,-1):
          y = y - 1
          unicorn.set_pixel(x,y,255,255,255)
          unicorn.show() # an
          time.sleep(0.5)
          unicorn.clear() 
      unicorn.set_pixel(x,y,255,255,255)
      unicorn.show() # an
      time.sleep(0.5)
      unicorn.clear() 
  
