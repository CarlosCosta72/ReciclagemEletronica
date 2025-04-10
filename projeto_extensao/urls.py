
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),  # Para a landing page principal
    path('', include('estoque.urls')),    # Inclui as URLs da aplicação estoque
]
