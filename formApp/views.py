from django.shortcuts import render,redirect
from .forms import FirstForm,EmpForm
from django.contrib import messages
from django.contrib.auth import login,logout
# Create your views here.
def addition(request):
    if request.method=='GET':
        emptyform=FirstForm()
        return render(request,'formapp/addition.html',{'form':emptyform})
    if request.method=='POST':
        data=FirstForm(request.POST)
        emptyform=FirstForm()
        if data.is_valid():
            v1=data.cleaned_data['value1']
            v2=data.cleaned_data['value2']
            res=v1+v2
            return render(request,'formapp/addition.html',{'res':res,'form':emptyform})
        else:
            return render(request,'formapp/addition.html',{'form':data})
def insertemp(request):
    if request.method=='GET':
        emptyform=EmpForm()
        return render(request,'formapp/insertemp.html',{'form':emptyform}) 
    if request.method=='POST':
        print(request.POST)
        emptyform=EmpForm()
        data=EmpForm(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request,'data inserted successfuly')
            #return render(request,'formapp/insertemp.html',{'form':emptyform})
            return redirect('selecturl')
            
        else:
            
            return render(request,'formapp/insertemp.html',{'form':data})
