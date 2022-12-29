from django.shortcuts import render
from django.http import *
from django.template import loader
from app.models import *
from django.shortcuts import render

def display (request):
    s1=int(input("credit value"))
    #double=subject.objects,values().order_by("-credit")
    dvalues = subject.objects.values().filter(credit=s1)
    #table values>(no of seconds)>values
    t=loader.get_template("display.html")
    c=dict({'dvalues':dvalues})
    return render(request,'display.html',c)

def input(request):
    t=loader.get_template("input.html")
    c=dict({'form':subject_form()})
    return render(request,'input.html',c)

def create_sub_det(request):
    if request.method=='POST':
        form=subject_form(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect('/detail/')

# Create your views here.
