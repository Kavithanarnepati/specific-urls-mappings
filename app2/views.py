from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<h1>django is used for developing web browsers</h1>')
def second(request):
    return HttpResponse('<h1>djano is used for developing dynamic web appilication</h1>')    