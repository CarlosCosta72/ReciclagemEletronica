from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.ComponenteListView.as_view(), name='componente_list'),
    path('incrementar/<int:pk>/', views.ComponenteListView.incrementar_componente, name='incrementar_componente'),
    path('decrementar/<int:pk>/', views.ComponenteListView.decrementar_componente, name='decrementar_componente'),
]
