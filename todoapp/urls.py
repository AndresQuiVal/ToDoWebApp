from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('add_todo/', views.add_todo_view),
    path('remove_todo/', views.remove_todo_view),
    path('about_todo/', views.about_todo_view),
]