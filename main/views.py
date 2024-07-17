from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/kot.html', {'title': 'kotiki'})

def info(request):
    return render(request, 'main/pios.html')

def family(request):
    return render(request, 'main/fam.html')

def felidae(request):
    return render(request, 'main/felidae.html')

def canidae(request):
    return render(request, 'main/canidae.html')