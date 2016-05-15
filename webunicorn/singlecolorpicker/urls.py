from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'choosename', views.choosename, name='choosename'),
    url(r'changergb', views.changeRGB, name='changeRGB'),
]
