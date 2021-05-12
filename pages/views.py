from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('This is a web page.')
# Create your views here.
