from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:prato_id>', views.churrasco, name='churrasco'),
    path('buscar/', views.buscar, name='buscar'),
]