# hello_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home'),  # Rota para a página inicial
    path('hello/', views.hello, name='hello'),  # Rota existente
]
