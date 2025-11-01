from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def info(request):
    return HttpResponse('good evening ' \
    'learn python full stack ' \
    'practicing daily ')
def display(request):
    return HttpResponse('good students daily practicing')
