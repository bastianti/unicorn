from django.shortcuts import render
from django.http import HttpResponse

#Import for unicorn Hat
import unicornhat as u
import time

def index(request):
    return HttpResponse("Hello World")


def choose(request):
    r = 0
    g = 0
    b = 0
    try:
        color = request.GET['color']
        u.brightness=1
	if color   == 'red':
	    r = 255
        elif color == 'blue':
	    b = 255
	elif color == 'green':
	    g = 255
	elif color == 'white':
	    r = 255
	    g = 255
	    b = 255
	for x in xrange(8):
	    for y in xrange(8):
	        u.set_pixel(x, y, r, g, b)
	u.show()
    except (KeyError):
        return render(request, 'singlecolorpicker/choose.html')
    return HttpResponse("Your choice was {0}".format(color))
    
