from io import TextIOBase
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
import pandas as pd
from csv import DictWriter

l1=[]
l2=[]

def index(request):
    if(len(l1)>=10):
        l1.clear()
        l2.clear()
    if request.method=="POST":

        form=request.POST

        a=float(form.get('Emissions'))
        b=float(form.get('Absorptions'))
        l1.append(a)
        l2.append(b)

    #return [yearList, emsListGraph, yearList, absListGraph, years, originalConc, yearList, totConcList]
    #lists
    #gloal variables
    #from to htlml
    #co2 current conseta
        yearList, emsListGraph, yearList, absListGraph, years, originalConc, yearList, totConcList=solve(l1,l2)
        cur = int((yearList[-1] - 1970)/10);
        print(years)
        plot_div1 = plot([Scatter(x=years, y=originalConc,
                            mode='lines', name='Concentration Goal',
                            opacity=1, marker_color='green',fill='tonexty'),Scatter(x=yearList, y=totConcList,
                            mode='lines', name='Simuated Concentration',
                            opacity=1, marker_color='Red',fill='toself')],
                   output_type='div')

        plot_div2 = plot([Scatter(x=yearList, y=emsListGraph,
                            mode='lines', name='emission',
                            opacity=0.8, marker_color='green'),Scatter(x=yearList, y=absListGraph,
                            mode='lines', name='absorption',
                            opacity=0.8, marker_color='Red')],
                   output_type='div')

        # plot_div2 = plot([Scatter(x=yearList, y=emsListGraph,
        #                     mode='lines', name='test',
        #                     opacity=0.8, marker_color='green'),bar(x=originalConc[cur],
        #                     mode='bar', name='test',
        #                     opacity=0.8, marker_color='Red')],
        #            output_type='div')


        fig = px.line(x=[0.5,1.5],y=[round(originalConc[cur],3),round(originalConc[cur],3)],labels=dict( y="Concentration"))
       # fig.add_bar(x=fruits, y=[2,1,3], name="Last year")
        fig.add_bar(x=[1],y = [totConcList[-1]])
        
        fig.update_traces(marker_color='orange')
        fig.update_yaxes(range=[totConcList[-1]-250,totConcList[-1]+250])
        

        plot_div3=plot(fig,output_type='div')
        form=data()
        print(originalConc)
        print(yearList)
        print(years)
        
        return render (request, "1.html",context={'form':form, 'plot_div1': plot_div1,'plot_div2': plot_div2,'plot_div3': plot_div3, 'year1':yearList[0],'year2':yearList[-1], 'co2_con':round(totConcList[-1],3),'co2_ab':round(absListGraph[-1],3),'co2_em':round(emsListGraph[-1],3),
        'goal_con':round(originalConc[cur],3),'goal_up':round(originalConc[cur],3)+0.5, 'goal_down':round(originalConc[cur],3)-0.5})
    else:
        form = data()

        yearList, emsListGraph, yearList, absListGraph, years, originalConc, yearList, totConcList=solve(l1,l2)
        plot_div1 = plot([Scatter(x=years, y=originalConc,
                            mode='lines', name='Concentration Goal',
                            opacity=0.8, marker_color='green',fill='tonexty'),Scatter(x=yearList, y=totConcList,
                            mode='lines', name='Simulated Concentration',
                            opacity=0.8, marker_color='Red',fill='toself')],
                   output_type='div')
        
        fig = px.line(x=[0.5,1.5],y=[round(originalConc[3],3),round(originalConc[3],3)],labels=dict( y="Concentration"))
        fig.add_bar(x=[1],y = [originalConc[3]])
        
        fig.update_traces(marker_color='orange')
        fig.update_yaxes(range=[originalConc[3]-250,originalConc[3]+250])
        

        plot_div3=plot(fig,output_type='div')
       


    l1.clear()
    l2.clear()
    return render(request,"1.html", context={'form':form, 'plot_div1':plot_div1,'plot_div3':plot_div3,'co2_con':round(originalConc[3],3),'co2_ab':4.077,'co2_em':8.155})


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
        
        
  
        # list of column names 
        field_names = ['name','email','Age',
                    'male','female','major']

        # Dictionary
        dict={'name':str(form.get('name')),'email':str(form.get('email')),'Age':str(form.get('Age')), 'male':str(form.get('male')),'female':str(form.get('female')),'major':str(form.get('select'))}
        # Open your CSV file in append mode
        # Create a file object for this file
        with open('/home/abhi/Work_temp/CS308/Group10/Group10/user_data/user.csv', 'a') as f_object:
            
        # Pass the file object and a list 
        # of column names to DictWriter()
        # You will get a object of DictWriter
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)

            #Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(dict)

        #Close the file object
            f_object.close()
            
        return redirect("/page1")

    return render (request, "user.html")


