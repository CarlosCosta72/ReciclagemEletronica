
from django.contrib import admin
from django.urls import path,include

from estoque.views import ComponenteListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('principal.urls')),
    path('', include('estoque.urls')),  
    path("", ComponenteListView.as_view()),
]
