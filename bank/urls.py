from django.urls import path

from . import views

from django.conf.urls import include,url
from django.conf import settings
from django.http import HttpResponseRedirect

urlpatterns = [
	url(r'^$',views.Main_page,name='Main_page'),
	url(r'^onetask',views.onetask,name='onetask'),
	url(r'^display',views.display,name='display'),
	url(r'^twotask',views.twotask,name='twotask'),
	url(r'^result',views.result,name='result'),
	
	#path('', views.index, name='index'),
]
