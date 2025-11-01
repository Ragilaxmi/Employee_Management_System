from django.urls import path
from . import views
urlpatterns=[
    path('',views.additon),
    path('genrate/',views.table),
]