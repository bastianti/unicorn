import unicornhat as u
from random import randint
import time
import sys

u.brightness(float(sys.argv[4]))
a=0
r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])
while True:
  for x in xrange(8):
    for y in xrange(8):
      print "u.set_pixel({0}, {1}, {2}, {3}, {4})".format(x,y,r,g,b)
      u.set_pixel(x,y,r,g,b)
  u.show()
  print "done"
  time.sleep(100)

