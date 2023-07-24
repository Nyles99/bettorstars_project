from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком туриниров
    path('tournaments/', views.tournaments_list),
    # Отдельная страница с информацией о конкретном турнире
    path('tournaments/<int:pk>/', views.tournaments_detail),
]
