from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from  . models import Employee,Department
from django.core.paginator import Paginator
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from DBApp.forms import RegisterForm
from . decorators import checkuser
# Create your views here. 
def dbprocess(request):
    return HttpResponse('db connected')
@checkuser
def dbinsert(request):
    if request.method=='GET':
        depts=Department.objects.all()
        return render(request,'dbapp/insert.html',{'departments':depts})
    if request.method=='POST':
        print(request.POST)
        print(request.FILES)
        eno=int(request.POST['eno'])
        ename=request.POST['ename']
        esal=int(request.POST['sal'])
        dptno=int(request.POST['dept'])
        pic=request.FILES['epic']
        video=request.FILES['video']
        dptobj=Department.objects.get(deptno=dptno)
        print(dptobj)
        depts=Department.objects.all()
        obj=Employee.objects.create(empno=eno,empname=ename,salary=esal,department=dptobj,profile_pic=pic,video=video)
        return redirect('selecturl',pno=1)
@login_required(login_url='loginurl')
def dbselect(request,pno):
    if request.method=='GET':
        emps=Employee.objects.select_related('department')
        Pcls_obj=Paginator(emps,5)
        page_obj=Pcls_obj.get_page(pno)
        return render(request,'dbapp/select.html',{'employee':page_obj})
def dbupdate(request,eno):
    def getemp(eno):
        empobj=Employee.objects.get(empno=eno)
        return empobj
    if request.method=='GET':
        empobj=getemp(eno)
        dptobj=Department.objects.all()
        return render(request,'dbapp/update.html',{'emprec':empobj,'departments':dptobj})
    if request.method=='POST':
        print(request.POST)
        empobj=getemp(eno)
        ename=request.POST['empname']
        esal=request.POST['empsal']
        dpt=int(request.POST['dept'])
        dobj=Department.objects.get(deptno=dpt)
        empobj.empname=ename
        empobj.salary=esal
        empobj.department=dobj
        empobj.save()
        return redirect('selecturl',pno=1)
def dbdelete(request,eno):
    if request.method=='GET':
        emp=get_object_or_404(Employee,empno=eno)
        return render(request,'dbapp/delete.html',{'emp':emp})
    if request.method=='POST':
        print(request.POST)
        emp=get_object_or_404(Employee,empno=eno)
        if request.POST['option']=='Yes':
            emp.delete()
            return redirect('selecturl',pno=1)    
        else:
            return redirect('selecturl',pno=1)

def portfolio(request,eno):
    emp=get_object_or_404(Employee,empno=eno)
    return render(request,'dbapp/portfolio.html',{'employee':emp})
    #return HttpResponse('request recieved')
def sessionexp(request):
        if 'cnt' in request.session:
            request.session['cnt']+=1
        else:
            request.session['cnt']=1
        print(request.session)
        return HttpResponse('session request recived'+str(request.session['cnt']))


def loginpage(request):
    if request.method=='GET':
        return render(request,'dbapp/login.html') 
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        uobj=authenticate(request,username=uname,password=pwd)
        if uobj is None:
           return redirect('loginurl')
        else:
           login(request,uobj)
           return redirect('selecturl',pno=1)
def logoutpage(request):
    logout(request)
    return redirect('loginurl')
        
def registerpage(request):
    if request.method=='GET':
        emptyform=RegisterForm()
        return render(request,'dbapp/register.html',{'form':emptyform})
    if request.method=='POST':
        dataobj=RegisterForm(request.POST)
        if dataobj.is_valid():
            dataobj.save()
            return redirect('loginurl')
        else:
            return render(request,'dbapp/register.html',{'form':dataobj})
        



    
        


        
