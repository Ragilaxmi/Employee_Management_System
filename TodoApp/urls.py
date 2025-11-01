from django.urls import path
from . import views

urlpatterns=[
    path('todoenter/',views.todocreate,name='todoenterurl'),
    path('tododelete/<str:item>/',views.tododelete,name='tododeleteurl'),
]