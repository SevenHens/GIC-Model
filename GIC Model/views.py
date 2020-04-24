from django.shortcuts import render
from rest_framework import viewsets
from . forms import PredictForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from . models import PredictModel
from . serializers import PredictSerializers
from django.http import HttpResponse
from django.conf import settings
import joblib
import pandas as pd
import numpy as np
import csv, io


class PredictView(viewsets.ModelViewSet):
    queryset = PredictModel.objects.all()
    serializer_class = PredictSerializers
        

def prediction(lt, model):
    try:
        x = (lt).transpose()
        x = x.iloc[:,2:66]
        y_pred = model.predict(x.values)
        newdf = pd.DataFrame(y_pred)
        newdf = newdf.replace({0: False, 1: True})
        return (newdf[0].values)
    except ValueError as e:
        return ("Bad Inputs")
 
def home(request):
    template = 'myform/home.html'
    return render(request, template)
    
def display_predict_renewal(request):
    template = "Display.html"
    model = joblib.load('C:/Users/e-sshen/Desktop/GIC Data/Renewal.pkl')
    
    if request.method == 'GET':
        return render(request, template)
    
    if request.method == 'POST':
        form = PredictForm(request.POST)
        csv_file = request.FILES["file"]
            
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload a .csv file')
        
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)
    results = []
    db = pd.read_csv('C:/Users/e-sshen/Desktop/GIC Data/ActiveHolders.csv')
    for col in csv.reader(io_string, delimiter = ',', quotechar = '|'):
        row = []
        display= []
        for i in db.values:
            if i[1] == int(col[0]) and i[2] == int(col[1]):
                row = i
        answer = prediction(pd.DataFrame(row), model)
        display.append(col[0])
        display.append(col[1])
        display.append(answer)
        results.append(display)
 
    data = pd.DataFrame(results)
    data_html = data.to_html(classes = ['table-bordered', 'table-striped', 'table-hover'])
    context = {'loaded_data': data_html,
                       'form':form}
    return render(request, template, context)

def display_predict_purchase(request):
    template = "Display.html"
    model = joblib.load('C:/Users/e-sshen/Desktop/GIC Data/Purchase.pkl')
    
    if request.method == 'GET':
        return render(request, template)
    
    if request.method == 'POST':
        form = PredictForm(request.POST)
        csv_file = request.FILES["file"]
            
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload a .csv file')
        
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)
    results = []
    db = pd.read_csv('C:/Users/e-sshen/Desktop/GIC Data/ActiveHolders.csv')
    for col in csv.reader(io_string, delimiter = ',', quotechar = '|'):
        row = []
        display= []
        for i in db.values:
            if i[1] == int(col[0]) and i[2] == int(col[1]):
                row = i
        answer = prediction(pd.DataFrame(row), model)
        display.append(col[0])
        display.append(col[1])
        display.append(answer)
        results.append(display)
 
    data = pd.DataFrame(results)
    data_html = data.to_html(classes = ['table-bordered', 'table-striped', 'table-hover'])
    context = {'loaded_data': data_html,
                       'form':form}
    return render(request, template, context)


def download_predict_purchase(request):
    template = "Download.html"
    model = joblib.load('C:/Users/e-sshen/Desktop/GIC Data/Purchase.pkl')
      
    if request.method == 'GET':
        return render(request, template)
    
    if request.method == 'POST':
        csv_file = request.FILES["file"]
            
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload a .csv file')
        
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)
    results = []
    db = pd.read_csv('C:/Users/e-sshen/Desktop/GIC Data/ActiveHolders.csv')
    for col in csv.reader(io_string, delimiter = ',', quotechar = '|'):
        row = []
        display= []
        for i in db.values:
            if i[1] == int(col[0]) and i[2] == int(col[1]):
                row = i
        answer = prediction(pd.DataFrame(row), model)
        display.append(col[0])
        display.append(col[1])
        display.append(answer)
        results.append(display)
        
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['Holder ID', 'Week', 'Answer'])
    for i in results:
        writer.writerow(i)
        
    response['Content-Disposition'] = 'attachment; filename = "WebsiteTestFileOutput.csv"'
    return response

def download_predict_renewal(request):
    template = "Download.html"
    model = joblib.load('C:/Users/e-sshen/Desktop/GIC Data/Renewal.pkl')
      
    if request.method == 'GET':
        return render(request, template)
    
    if request.method == 'POST':
        csv_file = request.FILES["file"]
            
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Please upload a .csv file')
        
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)
    results = []
    db = pd.read_csv('C:/Users/e-sshen/Desktop/GIC Data/ActiveHolders.csv')
    for col in csv.reader(io_string, delimiter = ',', quotechar = '|'):
        row = []
        display= []
        for i in db.values:
            if i[1] == int(col[0]) and i[2] == int(col[1]):
                row = i
        answer = prediction(pd.DataFrame(row), model)
        display.append(col[0])
        display.append(col[1])
        display.append(answer)
        results.append(display)
        
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['Holder ID', 'Week', 'Answer'])
    for i in results:
        writer.writerow(i)
        
    response['Content-Disposition'] = 'attachment; filename = "WebsiteTestFileOutput.csv"'
    return response

    
