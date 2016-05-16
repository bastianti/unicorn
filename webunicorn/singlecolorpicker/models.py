from __future__ import unicode_literals

from django.db import models

class RGBColor(models.Model):
    red_value           = models.SmallIntegerField(default=0)
    green_value         = models.SmallIntegerField(default=0)
    blue_value          = models.SmallIntegerField(default=0)
    human_readable_name = models.CharField(max_length=100)
    def __str__(self):
        return self.human_readable_name

class Brightness(models.Model):
    brightness          = models.SmallIntegerField(default=50)
    def __int__(self):
        return self.brightness


class LastColorValue(models.Model):
    red_value           = models.SmallIntegerField(default=0)
    green_value         = models.SmallIntegerField(default=0)
    blue_value          = models.SmallIntegerField(default=0)
