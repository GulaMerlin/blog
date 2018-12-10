from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^share/$', views.share, name='share'),
    url(r'^info/$', views.info, name='info')
]
