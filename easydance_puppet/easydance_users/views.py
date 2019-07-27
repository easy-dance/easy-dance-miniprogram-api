from django.shortcuts import render
from django.http import HttpResponse

def login(req):
    print('Login!')
    return HttpResponse('Login Success!')


# Create your views here.
