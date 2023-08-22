from django.urls import path
from . import views


app_name = 'tournaments'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком туриниров
    path('tournaments_list', views.tournaments_list, name='tournaments_list'),
    # Отдельная страница с информацией о конкретном турнире
    path('tournaments/<int:pk>/', views.tournaments_detail),
]
