from django.urls import path

from .views import *

urlpatterns = [
	#Leave as empty string for base url
	 path('',home, name= 'home' ),
	

]