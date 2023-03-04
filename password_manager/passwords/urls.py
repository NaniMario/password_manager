from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.passwords, name='passwords'),
    path('delete/<str:pk>', views.delete_password, name='delete'),
    path('edit/<str:pk>', views.edit_password, name='edit'),
    path('add/<str:pk>', views.add_password, name='add'),
]
