from django.urls import path
from .views import Index,Teste


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('teste', Teste.as_view(), name='teste'),
   
# CBV básica
    #path('minhaview/', MinhaView.as_view(), name='minha-view'),
    
    # TemplateView
    
    
    # ListView
   # path('itens/', ListaItensView.as_view(), name='lista-itens'),
    
    # DetailView com parâmetro na URL
   # path('item/<int:pk>/', DetalheItemView.as_view(), name='detalhe-item'),

]
