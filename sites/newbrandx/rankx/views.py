import sys
import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from chartit import DataPool, Chart
from .models import Milk
from .models import Brand
from .models import Company

def rankx(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'rankx/rankx.html')

def milk(request):
    report1 = datetime.date.today().strftime("rankx/reports/milk/milk_%Y_%m.html")
    report2 = datetime.date.today().strftime("rankx/reports/milk/milk_curve.html")
    context = { 'indexs' : Milk.objects.filter(pub_date__range = ('2013-10-24', '2015-10-31')),
                'report1' : report1,
                'report2' : report2,
            }
    return render(request, 'rankx/milk.html', context)

def milk_chart_view(request):
    json_file = datetime.date.today().strftime("templates/rankx/reports/milk/milk_%Y_%m.json")
    with open(json_file) as data_file:
        data = json.loads(data_file.read())
    return HttpResponse(json.dumps(data), content_type='application/json')

'''
def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response({'weatherchart': cht})

'''
def cloth(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def toy(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def edu(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def health(request):
    return HttpResponse("Hello, world. You're at the polls index.")
