from django.urls import path
from .views import (
    UsuarioListView, UsuarioCreateView,
    UsuarioUpdateView, UsuarioDeleteView
)

app_name = 'usuarios'

urlpatterns = [
    path('', UsuarioListView.as_view(), name='listar'),
    path('novo/', UsuarioCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', UsuarioUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>/', UsuarioDeleteView.as_view(), name='excluir'),
]
