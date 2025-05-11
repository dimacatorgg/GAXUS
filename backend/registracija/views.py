from django.shortcuts import render
from django.http import HttpResponse

def home(requests):
    return HttpResponse("Zdravo sa kraja sveta")

