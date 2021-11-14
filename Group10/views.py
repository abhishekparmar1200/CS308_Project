from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import os

#plotly
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px

import numpy as np
from .functions import *
from .forms import data

l1=[]
l2=[]

def index(request):
    if(len(l1)>=20):
        l1.clear()
        l2.clear()
    if request.method=="POST":

        form=request.POST

        a=int(form.get('Emissions'))
        b=int(form.get('Absorptions'))
        l1.append(a)
        l2.append(b)

    #return [yearList, emsListGraph, yearList, absListGraph, years, originalConc, yearList, totConcList]
    #lists
    #gloal variables
    #from to htlml
    #co2 current conseta
        yearList, emsListGraph, yearList, absListGraph, years, originalConc, yearList, totConcList=solve(l1,l2)
        cur = int((yearList[-1] - 1970)/10);
        plot_div1 = plot([Scatter(x=years, y=originalConc,
                            mode='lines', name='test',
                            opacity=0.8, marker_color='green'),Scatter(x=yearList, y=totConcList,
                            mode='lines', name='test',
                            opacity=0.8, marker_color='Red')],
                   output_type='div')

        plot_div2 = plot([Scatter(x=yearList, y=emsListGraph,
                            mode='lines', name='test',
                            opacity=0.8, marker_color='green'),Scatter(x=yearList, y=absListGraph,
                            mode='lines', name='test',
                            opacity=0.8, marker_color='Red')],
                   output_type='div')

        # plot_div2 = plot([Scatter(x=yearList, y=emsListGraph,
        #                     mode='lines', name='test',
        #                     opacity=0.8, marker_color='green'),bar(x=originalConc[cur],
        #                     mode='bar', name='test',
        #                     opacity=0.8, marker_color='Red')],
        #            output_type='div')

        fig = px.bar(x=[1],y = [totConcList[-1]])

        fig.update_traces(marker_color='orange')
        # fig1=Scatter(x=[0], y=[int(originalConc[cur])],
        #                     mode='lines', name='test',
        #                     opacity=0.8, marker_color='Red')

        plot_div3=plot(fig,output_type='div')
        form=data()
        print(yearList)
        return render (request, "1.html",context={'form':form, 'plot_div1': plot_div1,'plot_div2': plot_div2,'plot_div3': plot_div3, 'year1':yearList[0],'year2':yearList[-1], 'co2_con':totConcList[-1]})
    else:
        form = data()


    return render(request,"1.html", {'form':form})


def welcome(request):

    return render (request, "welcome.html")

def ins1(request):

    return render (request, "instruction1.html")


def ins2(request):

    return render (request, "instruction2.html")

def ins3(request):

    return render (request, "instruction3.html")

def test(request):

    return render (request, "test.html")


def user(request):

    if request.method=='POST':
        form=request.POST
        print(form.get('name'))
        print(form.get('email'))
        print(form.get('Age'))
        print(form.get('male'))
        print(form.get('female'))
        print(form.get('select'))
        return redirect("/page1")

    return render (request, "user.html")


