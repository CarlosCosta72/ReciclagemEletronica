from django.shortcuts import render

def index(request):
    return render(request, 'principal/index.html')

def contato(request):
    return render(request, 'principal/contato.html')

def quem_somos(request):
    return render(request, 'principal/quem_somos.html')
