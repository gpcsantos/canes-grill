from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Prato

# Create your views here.
def index(request):
    pratos = Prato.objects.filter(publicado=True).order_by('-date_prato')
    #print(pratos.query)
    
    contexto = {
        'lista_pratos' : pratos,
    }
    return render(request, 'index.html', contexto)

def churrasco(request, prato_id):
    # prato = Prato.objects.filter(pk=prato_id)   
    prato = get_object_or_404(Prato, pk=prato_id)
    
    contexto = {
        'prato' : prato,
    }
    return render(request, 'churrasco.html', contexto)
    
