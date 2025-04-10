from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.lista_estoque, name='lista_estoque'),
]