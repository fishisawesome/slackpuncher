from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^punch/$', views.json, name='json'),
	url(r'^$', views.index, name='index'),
]
