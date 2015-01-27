#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np

unicorn.brightness(1)

while True:
	rand_mat = np.random.rand(8,8)	
	for z in range(360):	
		for a in range(360):	
			for c in range(360):	
				for y in range(8):
					for x in range(8):
						rgb = colorsys.hsv_to_rgb(z/360.0,a/360.0,c/100)
						print rgb	
						r = int(rgb[0]*120.0)
						g = int(rgb[1]*120.0)
						b = int(rgb[2]*120.0)
						print x,y,r,g,b
						unicorn.set_pixel(x, y, r, g, b)
				unicorn.show()
				time.sleep(0.1)
