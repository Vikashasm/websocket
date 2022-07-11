from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show(request):
    return HttpResponse('hello sir your site is runnig well')