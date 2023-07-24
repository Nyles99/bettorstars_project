from django.urls import path
from . import views

urlpatterns = [
    # Страница с списком пользователей
    path('users/', views.users_list),
    # Страница о конкретном пользователе
    path('users/<int:pk>/', views.users_detail),
]
