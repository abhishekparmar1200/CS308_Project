from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import os

#plotly
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

def index(request):
    print(request.POST.get("Test"))
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    return render (request, "1.html",context={'plot_div': plot_div})


def welcome(request):

    return render (request, "welcome.html")

def ins1(request):

    return render (request, "instruction1.html")


def ins2(request):

    return render (request, "instruction2.html")

def ins3(request):

    return render (request, "instruction3.html")


def user(request):

    print(request.POST)

    return render (request, "user.html")


