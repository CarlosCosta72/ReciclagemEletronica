from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
]