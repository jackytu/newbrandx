from django.shortcuts import render
from django.http import HttpResponse


def rankx(request):
        #return HttpResponse("Hello, world. You're at the polls index.")
        return render(request, 'rankx/rankx.html')
def milk(request):
        return render(request, 'rankx/milk.html')
def cloth(request):
        return render(request, 'rankx/cloth.html')
def toy(request):
        return render(request, 'rankx/toy.html')
def edu(request):
        return render(request, 'rankx/edu.html')
def health(request):
        return render(request, 'rankx/health.html')
