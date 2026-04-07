from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView


class Index(TemplateView):
    template_name = 'app/index.html'

class Teste(TemplateView):
    template_name = 'app/mapa_votos_final.html'

'''
class ListaItensView(ListView):
    model = MinhaModel
    template_name = 'meuapp/lista.html'
    context_object_name = 'itens'

class DetalheItemView(DetailView):
    model = MinhaModel
    template_name = 'app/detalhe.html'
    context_object_name = 'item'

'''