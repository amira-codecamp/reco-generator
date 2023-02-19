from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='main-view'),
    path('pdf/', views.pdf, name='pdf'),
    path('word/', views.word, name='word'),
]