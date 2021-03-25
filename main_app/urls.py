 # main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('bubble/', views.bubble, name='bubble'),
    path('water/', views.water_index, name='water')
]