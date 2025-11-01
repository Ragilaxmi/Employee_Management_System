from django.shortcuts import redirect
def checkuser(f):
    def innerfun(req):
        if req.user.is_superuser:
            return f(req)
        else:
            return redirect('selecturl',pno=1)
    return innerfun 