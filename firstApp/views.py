from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    obj=HttpResponse('Hello world')
    return obj 
def show(request):
    return HttpResponse('we are good students')
def info(request):
    return HttpResponse('hello world')