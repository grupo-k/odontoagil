from django.urls import path
from .views import (
    HistoriaListView, HistoriaCreateView,
    HistoriaUpdateView, HistoriaDeleteView
)

app_name = 'historias'

urlpatterns = [
    path('', HistoriaListView.as_view(), name='listar'),
    path('nova/', HistoriaCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', HistoriaUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>/', HistoriaDeleteView.as_view(), name='excluir'),
]
