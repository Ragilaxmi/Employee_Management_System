from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('registerapi/',views.registerapi),
    path('loginapi/',obtain_auth_token),
    path('getemployee/',views.getempapi),
    path('getemp/',views.getemployeeapi),
    path('modifyapi/<int:pk>/',views.modifyapi),
    path('deleteapi/<int:pk>/',views.modifyapi),
    ]