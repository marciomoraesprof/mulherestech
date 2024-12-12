from django.shortcuts import render
from .models import Produto
from django.http import HttpResponse

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def sobre(request):
    return render(request, 'pagina2.html')

def produto(request):
    produtos = Produto.objects.all()
    if produtos:
        return HttpResponse("Deu merda")
    
    return HttpResponse("Teste funcionou")