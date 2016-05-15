import unicornhat as u
from random import randint
import time

u.brightness(0.5)
a=0
#while True:
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
while True:
  x = randint(0, 7)
  y = randint(0, 7)
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  #print "u.set_pixel({0}, {1}, {2}, {3}, {4})".format(x,y,r,g,b)
  u.set_pixel(x,y,r,g,b)
  u.show()
  a = a +1
# if a%80 == 0:
#    u.clear()
  time.sleep(1)


