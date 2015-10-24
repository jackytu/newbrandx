from django.shortcuts import render
from django.http import HttpResponse
from .models import MilkIndex

def rankx(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'rankx/rankx.html')
def milk(request):
    context = { 'indexs' : MilkIndex.objects.filter(index__gte = 0)}
    return render(request, 'rankx/milk.html', context)
def cloth(request):
    return render(request, 'rankx/cloth.html')
def toy(request):
    return render(request, 'rankx/toy.html')
def edu(request):
    return render(request, 'rankx/edu.html')
def health(request):
    return render(request, 'rankx/health.html')
