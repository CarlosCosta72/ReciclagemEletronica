from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.ComponenteListView.as_view(), name='componente_list'),
]
