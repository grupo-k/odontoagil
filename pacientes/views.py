from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm

class PacienteListView(ListView):
    model = Paciente
    template_name = 'pacientes/listar.html'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'form.html'
    success_url = reverse_lazy('pacientes:listar')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'form.html'
    success_url = reverse_lazy('pacientes:listar')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('pacientes:listar')
