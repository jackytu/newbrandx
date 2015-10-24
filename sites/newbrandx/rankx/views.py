from django.shortcuts import render
from django.http import HttpResponse
from .models import Milk
from .models import Brand
from .models import Company

def rankx(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'rankx/rankx.html')

def milk(request):
    context = { 'indexs' : Milk.objects.filter(pub_date__range = (2013-10-24, 2015-10-31))}
    return render(request, 'rankx/milk.html', context)

def cloth(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def toy(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def edu(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def health(request):
    return HttpResponse("Hello, world. You're at the polls index.")
