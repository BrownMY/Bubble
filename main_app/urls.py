 # main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('water/', views.water_index, name='water'),
    path('water/<int:water_id>/', views.water_show, name='water_show')
] 