app_name='anything'
from django.urls import path
from app1.views import *
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]