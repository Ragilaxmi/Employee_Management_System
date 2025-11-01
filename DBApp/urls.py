from django.urls import path
from . import  views

urlpatterns=[
    path('',views.dbprocess),
    path('insert/',views.dbinsert,name='inserturl'),
    path('select/<int:pno>/',views.dbselect,name='selecturl'),
    path('update/<int:eno>/',views.dbupdate,name='updateurl'),
    path('delete/<int:eno>/',views.dbdelete,name='deleteurl'),
    path('session/',views.sessionexp),
    path('portfolio/<int:eno>/',views.portfolio,name='portfolioURL'),
    path('login/',views.loginpage,name='loginurl'),
    path('logout/',views.logoutpage,name='logouturl'),
    path('register/',views.registerpage,name='registerurl'),
    
    
    
]