from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def additon(request):
    if request.method=="GET":
        obj=render(request,'calculatorApp/addition.html',)
        return obj
    if request.method=="POST":
        print(request.POST)
        #return HttpResponse('sent successfuly your data')
        
        a=int(request.POST['t1'])
        b=int(request.POST['t2'])
        if 'add' in request.POST:
            result=a+b
            action='addition'
        elif 'sub' in request.POST:
            result=a-b
            action='substraction'
        elif 'div' in request.POST:
            result=a/b
            action='division'
        else:
            result=a*b
            action='multiplication'
        return render(request,'calculatorApp/addition.html',{'result':result,'action':action})
    
def table(request):
    if request.method=='GET':
        return render(request,'calculatorApp/mtable.html')
    if request.method=="POST":
        lst=[]
        num=request.POST['number']

        for i in range(1,11):
            t=str(num)+'*'+str(i)+'='+str(int(num)*i)
            lst.append(t)
        return render(request,'calculatorApp/mtable.html',{'lst':lst})


