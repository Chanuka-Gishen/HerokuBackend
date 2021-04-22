from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Connected")

def getLankaProperty(request):
    return HttpResponse("https://www.lankapropertyweb.com/")

def getIkmanLk(request):
    return HttpResponse("https://ikman.lk/")

def getCeylonProperty(request):
    return HttpResponse("https://www.ceylonproperty.lk/")

