from django.urls import path
from . import views

urlpatterns=[
    path('addition/',views.addition),
    path('empenter/',views.insertemp),
    path('login/',views.login),
]