from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first(request):
    return HttpResponse('<h1><marquee> hi   good morning </marquee></h1>')
def second(request):
    return HttpResponse('<h2><marquee>i love django </marquee></h2>')    