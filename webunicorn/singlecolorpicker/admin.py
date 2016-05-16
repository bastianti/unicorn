from django.contrib import admin

from .models import RGBColor, Brightness, LastColorValue

admin.site.register(RGBColor)
admin.site.register(Brightness)
admin.site.register(LastColorValue)
