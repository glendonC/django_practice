from django.urls import path
from . import views

urlpatterns = [

    #sends user to views.py index function
    path('', views.index),
    path('add/', views.add),
]
