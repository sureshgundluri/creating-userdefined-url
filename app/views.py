from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getjob(request):
    return HttpResponse('searching for job')