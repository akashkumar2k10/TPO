from django.urls import path
from .views import *


urlpatterns=[
	path('',index2,name='index'),
]