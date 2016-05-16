from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import RGBColor, Brightness, LastColorValue

#Import for unicorn Hat
import unicornhat as u
import time

def index(request):
    return HttpResponse("Hello World")


def choosename(request):
    try:
	brightness = float(request.GET['brightness'])/100
        u.brightness(brightness)      
        color = request.GET['color']
	if color   == 'red':
	    r = 255
            g = 0
            b = 0
        elif color == 'blue':
	    b = 255
            g = 0
            r = 0
	elif color == 'green':
	    g = 255
            r = 0
            b = 0
	elif color == 'white':
	    r = 255
	    g = 255
	    b = 255
	elif color == 'off':
	    r = 0
	    g = 0
	    b = 0
	
	for x in xrange(8):
	    for y in xrange(8):
	        u.set_pixel(x, y, r, g, b)
	u.show()
    except (KeyError):
	u.show()
        return render(request, 'singlecolorpicker/choose.html')
    return render(request, 'singlecolorpicker/choose.html')


def changeRGB(request):
    color_list = RGBColor.objects.all()

    # Save old Values
    brightnessobj = Brightness.objects.filter(pk=1)[0]
    brightness = brightnessobj.brightness 
    lastcolorvalueobj = LastColorValue.objects.filter(pk=1)[0]
    red   = lastcolorvalueobj.red_value 
    green = lastcolorvalueobj.green_value 
    blue  = lastcolorvalueobj.blue_value 

    try:
        try:
            colorobj = RGBColor.objects.filter(human_readable_name=request.POST['color'])[0]
            red   = colorobj.red_value
            green = colorobj.green_value
            blue  = colorobj.blue_value
            human_readable_name = colorobj.human_readable_name
            print "Red: {0}".format(colorobj.red_value)
            print "Green: {0}".format(colorobj.green_value)
            print "Blue: {0}".format(colorobj.blue_value)
            print "Brightness {0}".format(brightness)
            lastcolorvalueobj.red_value           = red
            lastcolorvalueobj.green_value         = green
            lastcolorvalueobj.blue_value          = blue
            lastcolorvalueobj.human_readable_name = human_readable_name

            lastcolorvalueobj.save()
        except:
            pass # This may happen

        brightnessobj.brightness = request.POST['brightness']
        brightnessobj.save()
        brightness = brightnessobj.brightness 

        u.brightness(float(brightness)/100)
    
        for x in xrange(8):
	    for y in xrange(8):
               u.set_pixel(x, y, red, green, blue)
               print "Setting pixel {0} {1} {2} {3} {4}, brightness: {5}".format(x, y, red, green, blue, float(brightness)/100)
	u.show()
    except(KeyError):
        template = loader.get_template('singlecolorpicker/changeRGB.html')
        context = {
            'color_list':color_list.order_by('human_readable_name'),
            'last_color':lastcolorvalueobj.human_readable_name,
            'brightness':brightness
        }
        return HttpResponse(template.render(context, request))
    template = loader.get_template('singlecolorpicker/changeRGB.html')
    context = {
        'color_list':color_list.order_by('human_readable_name'),
        'last_color':lastcolorvalueobj.human_readable_name,
        'brightness':brightness
    }
    return HttpResponse(template.render(context, request))
 
