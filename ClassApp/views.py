from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView,UpdateView
from DBApp.models import Employee
from django.views.generic import ListView
from django.urls import reverse_lazy
# Create your views here.
class FirstView(View):
    def get(self,request):
        return render(request,'classapp/addition.html')
    def post(self,request):
        v1=int(request.POST['a'])
        v2=int(request.POST['b'])
        res=v1+v2
        return render(request,'classapp/addition.html',{'res':res})
class SecondView(FirstView):
    def post(self,request):
        v1=int(request.POST['a'])
        v2=int(request.POST['b'])
        res=v1*v2
        return render(request,'classapp/addition.html',{'res':res})
class InserView(CreateView):
    model=Employee
    fields='__all__'
    template_name='classapp/insert.html'
    def get_success_url(self):
        return reverse_lazy('selecturl',args=[1])
class SelectView(ListView):
    model=Employee
    template_name='classapp/select.html'
class ModifyView(UpdateView):
    model=Employee
    fields='__all__'
    template_name='classapp/update.html'
    success_url=reverse_lazy('selecturl',args=[1])