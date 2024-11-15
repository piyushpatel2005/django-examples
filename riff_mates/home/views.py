from sys import version
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def credits (request):
    content = "Nicky\nYour Name"
    return HttpResponse(content)

def about (request):
    content = "<h1>About</h1>"
    return HttpResponse(content)

def version_info (request):
    content = {"version" : "1.0"}
    return JsonResponse(content)