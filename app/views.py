from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
def display(request):
    ins=StudentForm()
    d={'ins':ins}
    if request.method=='POST':
        dd=StudentForm(request.POST)
        if dd.is_valid():
            a=dd.cleaned_data["Name"]
            b=dd.cleaned_data["Age"]
            c=dd.cleaned_data["Url"]
            SO=Student.objects.get_or_create(Name=a,Age=b,Url=c)[0]
            SO.save()
            SQS=Student.objects.all()
            d1={"SQS":SQS}
            return render(request,'dinfo.html',d1)
    return render(request,'django.html',d)