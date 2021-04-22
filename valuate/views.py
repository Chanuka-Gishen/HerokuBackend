from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from valuate.serializers import UserInputSerializer
from valuate.models import UserValuationDetails
import json
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

input_data = []

def index(response):
    return HttpResponse("Connected")

def getCity(response, city):
    return HttpResponse("City is {}".format(city))

@csrf_exempt
def export_csv(request):
    user_data=JSONParser().parse(request)
    data = user_data
    
    with open('writeData.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #way to write to csv file
        writer.writerow(["Distance_Nearest_Town","Perch","Year"])
        writer.writerow(data)
    print(data)
    return JsonResponse(data, safe= False)

def give_predictions(response):
    lr=LinearRegression()

    df=pd.read_csv("Galle_train_data.csv")
    df.head()

    z=df[['Distance_Nearest_Town','Perch','Year']]
    lr.fit(z,df['Value_of_one_perch'])

    lr.intercept_
    lr.coef_[1]

    dfin=pd.read_csv("writeData.csv")

    dfin.head()

    output=lr.intercept_+lr.coef_[0]*dfin.at[0,'Distance_Nearest_Town']+lr.coef_[1]*dfin.at[0,'Perch']+lr.coef_[2]*dfin.at[0,'Year']
    num = round(output, 2)
    return HttpResponse(num)

@csrf_exempt
def get_valuate_inputs(request):
    user_inputs = JSONParser().parse(request)
    user_input_serializer = UserInputSerializer(data=user_inputs)
    if user_input_serializer.is_valid():
        user_input_serializer.save()
        return JsonResponse("Input Saved successfully..!" , safe=False)
    return JsonResponse("Failed to Add.",safe=False)

@csrf_exempt
def get_saved_inputs(request):
    data = UserValuationDetails.objects.all()
    user_serializer = UserInputSerializer(data, many=True)
    return JsonResponse(user_serializer.data, safe=False)

@csrf_exempt
def land_detail(request):
    user_data = JSONParser().parse(request)
    data = user_data
    landType = data[0]
    distance = int(data[1])
    generate_str = ""
    if distance <= 2 and landType == "Bare Land":
        generate_str = "Bare lands are areas with no dominant vegetation cover on at least 90 percent of the area.Because of the distance from the location to the town it is suitable for use as a bussiness location.Not really suitable for a place to live."
    if 2 < distance < 7 and landType == "Wetland":
        generate_str = "wetland is an area of land that is either covered by water or saturated with water. Inside this range in galle we have famous schools near by, but location like this is not suitable for living except you build the surface."  

    return HttpResponse(generate_str)

