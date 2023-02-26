from django.urls import path
from . import views

urlpatterns = [

    #sends user to views.py index function
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('profile/', views.profile, name='profile'),
]
