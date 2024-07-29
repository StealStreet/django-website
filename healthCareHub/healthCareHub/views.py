from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, World! This is the healthCareHub homepage.')
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('Hello, World! This is the healthCareHub about page.')


def contact(request):
    return HttpResponse('Hello, World! This is the healthCareHub contact page.')

