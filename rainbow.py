#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys

print("Some LEDs wont light up in this example.")
print("Don't panic!")

unicorn.brightness(0.1)

while True:
	for z in range(360):
		for y in range(8):
			for x in range(8):

				rgb = colorsys.hsv_to_rgb(z/360.0,y/7.0,x/7.0)
                                print rgb
				r = int(rgb[0]*255.0)
				g = int(rgb[1]*255.0)
				b = int(rgb[2]*255.0)
				unicorn.set_pixel(x,y,r,g,b)
		unicorn.show()
