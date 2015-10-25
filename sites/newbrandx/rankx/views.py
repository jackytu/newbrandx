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
    report3 = datetime.date.today().strftime("rankx/reports/milk/milk_best.html")
    context = { 'indexs' : Milk.objects.filter(pub_date__range = ('2013-10-24', '2015-10-31')),
                'report1' : report1,
                'report2' : report2,
                'report3' : report3,
            }
    return render(request, 'rankx/milk.html', context)

def milk_chart_view(request):
    json_file = datetime.date.today().strftime("templates/rankx/reports/milk/milk_%Y_%m.json")
    with open(json_file) as data_file:
        data = json.loads(data_file.read())
    return HttpResponse(json.dumps(data), content_type='application/json')

def cloth(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def toy(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def edu(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def health(request):
    return HttpResponse("Hello, world. You're at the polls index.")
