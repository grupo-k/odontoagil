from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario
from .forms import UsuarioForm

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/listar.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('usuarios:listar')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('usuarios:listar')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('usuarios:listar')
