from django.contrib import admin
from django.urls import path, include
from pro1app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.details, name='details'),
]
