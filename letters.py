import unicornhat as u
from random import randint
import time
import sys

u.brightness(1)
#Plug on top
u.rotation(180)

def print_letter_line(matrix, row, x=0, r=255, g=0, b=0):
  for dot in matrix:
    if dot == 1:
      try: 
        u.set_pixel(x, row, r, g, b)
      except:
        pass
#      print "u.set_pixel({0},0,255,0,0,0)".format(x)
    x = x+1

##Letter A
a1 = [0,0,1,1,1,1,1,1]
a2 = [0,0,1,0,0,0,0,1]
a3 = [0,0,1,0,0,0,0,1]
a4 = [0,0,1,1,1,1,1,1]
a5 = [0,0,1,0,0,0,0,1]
a6 = [0,0,1,0,0,0,0,1]
a7 = [0,0,1,0,0,0,0,1]
a8 = [0,0,1,0,0,0,0,1]

##Letter B
b1 = [0,1,1,1,0,0,0,0]
b2 = [0,1,0,0,1,0,0,0]
b3 = [0,1,0,0,1,0,0,0]
b4 = [0,1,0,0,1,0,0,0]
b5 = [0,1,1,1,0,0,0,0]
b6 = [0,1,0,0,1,0,0,0]
b7 = [0,1,0,0,1,0,0,0]
b8 = [0,1,1,1,0,0,0,0]

##Letter S
s1 = [0,0,0,1,1,1,0,0]
s2 = [0,0,1,0,0,0,0,0]
s3 = [0,0,1,0,0,0,0,0]
s4 = [0,0,1,0,0,0,0,0]
s5 = [0,0,0,1,1,0,0,0]
s6 = [0,0,0,0,0,1,0,0]
s7 = [0,0,0,0,0,1,0,0]
s8 = [0,0,1,1,1,0,0,0]

##Letter T
t1 = [0,1,1,1,1,1,1,1]
t2 = [0,0,0,0,1,0,0,0]
t3 = [0,0,0,0,1,0,0,0]
t4 = [0,0,0,0,1,0,0,0]
t5 = [0,0,0,0,1,0,0,0]
t6 = [0,0,0,0,1,0,0,0]
t7 = [0,0,0,0,1,0,0,0]
t8 = [0,0,0,0,0,0,0,0]

##Letter I
i1 = [0,0,0,1,1,1,0,0]
i2 = [0,0,0,0,1,0,0,0]
i3 = [0,0,0,0,1,0,0,0]
i4 = [0,0,0,0,1,0,0,0]
i5 = [0,0,0,0,1,0,0,0]
i6 = [0,0,0,0,1,0,0,0]
i7 = [0,0,0,0,1,0,0,0]
i8 = [0,0,0,1,1,1,0,0]

##Letter C
c1 = [0,0,0,1,1,1,0,0]
c2 = [0,0,1,0,0,0,0,0]
c3 = [0,1,0,0,0,0,0,0]
c4 = [0,1,0,0,0,0,0,0]
c5 = [0,1,0,0,0,0,0,0]
c6 = [0,1,0,0,0,0,0,0]
c7 = [0,0,1,0,0,0,0,0]
c8 = [0,0,0,1,1,1,0,0]

##Letter L
l1 = [0,0,1,0,0,0,0,0]
l2 = [0,0,1,0,0,0,0,0]
l3 = [0,0,1,0,0,0,0,0]
l4 = [0,0,1,0,0,0,0,0]
l5 = [0,0,1,0,0,0,0,0]
l6 = [0,0,1,0,0,0,0,0]
l7 = [0,0,1,0,0,0,0,0]
l8 = [0,0,1,1,1,1,1,0]

##Letter R
r1 = [1,1,1,1,0,0,0,0]
r2 = [1,0,0,0,1,0,0,0]
r3 = [1,0,0,0,1,0,0,0]
r4 = [1,0,1,1,0,0,0,0]
r5 = [1,0,1,0,0,0,0,0]
r6 = [1,0,0,1,0,0,0,0]
r7 = [1,0,0,0,1,0,0,0]
r8 = [1,0,0,0,0,1,0,0]

def print_a(offset=0):
  print_letter_line(a1,0, offset)
  print_letter_line(a2,1, offset)
  print_letter_line(a3,2, offset)
  print_letter_line(a4,3, offset)
  print_letter_line(a5,4, offset)
  print_letter_line(a6,5, offset)
  print_letter_line(a7,6, offset)
  print_letter_line(a8,7, offset)
 
def print_b(offset=0):
  print_letter_line(b1,0, offset)
  print_letter_line(b2,1, offset)
  print_letter_line(b3,2, offset)
  print_letter_line(b4,3, offset)
  print_letter_line(b5,4, offset)
  print_letter_line(b6,5, offset)
  print_letter_line(b7,6, offset)
  print_letter_line(b8,7, offset)

def print_s(offset=0):
  r = 0
  g = 180
  b = 0
  print_letter_line(s1,0, offset, r, g, b)
  print_letter_line(s2,1, offset, r, g, b)
  print_letter_line(s3,2, offset, r, g, b)
  print_letter_line(s4,3, offset, r, g, b)
  print_letter_line(s5,4, offset, r, g, b)
  print_letter_line(s6,5, offset, r, g, b)
  print_letter_line(s7,6, offset, r, g, b)
  print_letter_line(s8,7, offset, r, g, b)

def print_t(offset=0):
  print_letter_line(t1,0, offset)
  print_letter_line(t2,1, offset)
  print_letter_line(t3,2, offset)
  print_letter_line(t4,3, offset)
  print_letter_line(t5,4, offset)
  print_letter_line(t6,5, offset)
  print_letter_line(t7,6, offset)
  print_letter_line(t8,7, offset)

def print_i(offset=0):
  print_letter_line(i1,0, offset)
  print_letter_line(i2,1, offset)
  print_letter_line(i3,2, offset)
  print_letter_line(i4,3, offset)
  print_letter_line(i5,4, offset)
  print_letter_line(i6,5, offset)
  print_letter_line(i7,6, offset)
  print_letter_line(i8,7, offset)

def print_c(offset=0):
  print_letter_line(c1,0, offset)
  print_letter_line(c2,1, offset)
  print_letter_line(c3,2, offset)
  print_letter_line(c4,3, offset)
  print_letter_line(c5,4, offset)
  print_letter_line(c6,5, offset)
  print_letter_line(c7,6, offset)
  print_letter_line(c8,7, offset)

def print_l(offset=0):
  print_letter_line(l1,0, offset)
  print_letter_line(l2,1, offset)
  print_letter_line(l3,2, offset)
  print_letter_line(l4,3, offset)
  print_letter_line(l5,4, offset)
  print_letter_line(l6,5, offset)
  print_letter_line(l7,6, offset)
  print_letter_line(l8,7, offset)

def print_r(offset=0):
  print_letter_line(r1,0, offset)
  print_letter_line(r2,1, offset)
  print_letter_line(r3,2, offset)
  print_letter_line(r4,3, offset)
  print_letter_line(r5,4, offset)
  print_letter_line(r6,5, offset)
  print_letter_line(r7,6, offset)
  print_letter_line(r8,7, offset)

def print_basti():
  for a in range(9,-40,-1):
    shift = 0
    print_b(a+shift)
    shift = shift + 6
    print_a(a+shift)
    shift = shift + 8
    print_s(a+shift)
    shift = shift + 8
    print_t(a+shift)
    shift = shift + 8
    print_i(a+shift)
    shift = shift + 8
    u.show()
    time.sleep(0.1)
    u.clear()

def print_clarissa():
  for a in range(9,-68,-1):
    shift = 0
    print_c(a+shift)
    shift = shift+8
    print_l(a+shift)
    shift = shift+8
    print_a(a+shift)
    shift = shift+12
    print_r(a+shift)
    shift = shift+8
    print_i(a+shift)
    shift = shift+8
    print_s(a+shift)
    shift = shift+8
    print_s(a+shift)
    shift = shift+8
    print_a(a+shift)
    shift = shift+8
    u.show()
    time.sleep(0.1)
    u.clear()


while True:
  print_basti()
  print_clarissa()




