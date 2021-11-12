from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    if(request.POST.get("Test")=='w'):
        return render(request,"home.html")
    print("AHHAHAHAHAH")
    return render (request, "1.html")


