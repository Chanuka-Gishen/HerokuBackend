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

<<<<<<< HEAD
@csrf_exempt
=======
>>>>>>> 57010dc66c7dfd8b11e12266fe8d17c721db3e6a
def get_saved_inputs(request):
    data = UserValuationDetails.objects.all()
    user_serializer = UserInputSerializer(data, many=True)
    return JsonResponse(user_serializer.data, safe=False)

