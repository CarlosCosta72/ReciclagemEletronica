from django.shortcuts import render
from .models import Componente

def lista_estoque(request):
    componentes = Componente.objects.all() 
    context = {'componentes': componentes}
    return render(request, 'estoque/lista_estoque.html', context)


