from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
class CustomMiddleware:
    def __init__(self,fun):
        self.get_response=fun
    def __call__(self,request):
        
        if request.method=='POST' and 'db/insert' in request.path_info :
            print(request.path_info)
            if int(request.POST['sal'])<0:
                #return HttpResponse('error')
                #raise ValidationError('negitive salary is not allowed')
                messages.error(request,'nagitive values are not allowed')
                return redirect('selecturl')
            
            else:
                messages.success(request,'successfully inserted')
        elif request.method=='POST' and 'form/addition' in request.path_info:
            pass 
        res=self.get_response(request)
        return res
                
            
            
        
        
