from django.shortcuts import render,redirect
# Create your views here.

def todocreate(request):
    if request.method=='GET':
        return render(request,'todoapp/todoinsert.html')
    if request.method=='POST':
        request.session.modified=True
        item=request.POST['t1']
        if 'items' in request.session:
            if item  not in request.session['items']:
                request.session['items'].append(item)
        
        else:
            request.session['items']=[item]
        return render(request,'todoapp/todoinsert.html',{'items':request.session['items']})
def tododelete(request,item):
        request.session.modified=True  
        if 'items' in request.session:
            request.session['items'].remove(item)  
            return redirect('todoenterurl')
        #return  render(request,'todoapp/todoinsert.html',{'items':request.session['items']})
    


