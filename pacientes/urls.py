from django.urls import path
from .views import (
    PacienteListView, PacienteCreateView,
    PacienteUpdateView, PacienteDeleteView
)

app_name = 'pacientes'

urlpatterns = [
    path('', PacienteListView.as_view(), name='listar'),
    path('novo/', PacienteCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', PacienteUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>/', PacienteDeleteView.as_view(), name='excluir'),
]
