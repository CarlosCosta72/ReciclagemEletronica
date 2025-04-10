from django.shortcuts import redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
from django.views.generic import ListView

from .models import componente

class ComponenteListView(ListView):
    model = componente
    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            nome = request.POST.get('nome')
            quantidade = request.POST.get('quantidade')
            descricao = request.POST.get('descricao')

            componente.objects.create(nome=nome, quantidade=quantidade, descricao=descricao)
        return redirect('componente_list')
    def incrementar_componente(request, pk):
        try:
            with transaction.atomic():
                componente_obj = get_object_or_404(componente, pk=pk)
                componente_obj.quantidade += 1
                componente_obj.save()
        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {e}")
        return redirect('componente_list')

    def decrementar_componente(request, pk):
        try:
            with transaction.atomic():
                componente_obj = get_object_or_404(componente, pk=pk)
                if componente_obj.quantidade > 0:
                    componente_obj.quantidade -= 1
                    componente_obj.save()
        except Exception as e:
            messages.error(request, f"Ocorreu um erro: {e}")
        return redirect('componente_list')
