from django.urls import path
from .import views


urlpatterns=[
    path('hi/',views.display),
    path('vcube/',views.show),
    path('',views.info),
]