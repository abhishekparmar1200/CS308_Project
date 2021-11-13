from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import os

def index(request):
    print(request.POST.get("Test"))

    if(request.POST.get("Test")=='w'):
        return render(request,"home.html")
    print("AHHAHAHAHAH")
    return render (request, "1.html")


