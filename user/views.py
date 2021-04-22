from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse

from user.models import UserDetails
from user.serializers import UserSerializer

# Create your views here.
@csrf_exempt
def addUserApi(request,id=0):
    user_data=JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse("Added Successfully!!" , safe=False)
    return JsonResponse("Failed to Add.",safe=False)
        
    
def getusers(request):
    users = UserDetails.objects.all()
    user_serializer = UserSerializer(users, many=True)
    return JsonResponse(user_serializer.data, safe=False)

def index(request):
    return HttpResponse("Curd Opertations")

def loancalculator(request):
    return HttpResponse("Connected")

        


    
