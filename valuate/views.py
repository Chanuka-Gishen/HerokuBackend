from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    input_data = user_inputs
    return HttpResponse("Input Saved successfully..!")

