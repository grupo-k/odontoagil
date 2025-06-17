from django.urls import path
from .views import (
    ServicoListView, ServicoCreateView,
    ServicoUpdateView, ServicoDeleteView,
    AtendimentoListView, AtendimentoCreateView
)

app_name = 'servicos'

urlpatterns = [
    path('', ServicoListView.as_view(), name='listar'),
    path('novo/', ServicoCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', ServicoUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>/', ServicoDeleteView.as_view(), name='excluir'),

    path('atendimentos/', AtendimentoListView.as_view(), name='atendimentos_listar'),
    path('atendimentos/novo/', AtendimentoCreateView.as_view(), name='atendimentos_criar'),
]
