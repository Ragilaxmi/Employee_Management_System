from django.urls import path
from . import views 
urlpatterns=[
    path('addition/',views.FirstView.as_view()),
    path('multiplication/',views.SecondView.as_view()),
    path('insert/',views.InserView.as_view()),
    path('select/',views.SelectView.as_view()),
    path('update/<int:pk>/',views.ModifyView.as_view())
]