from django.db import models
from django import forms


# Create your models here.

class subject(models.Model):#table name for database
    sname=models.CharField(max_length=50)
    scode=models.CharField(max_length=10)
    credit=models.IntegerField()

class subject_form(forms.ModelForm):
    class Meta:#meta default name 
        model=subject
        exclude=()
