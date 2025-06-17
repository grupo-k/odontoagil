from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import HistoriaClinica
from .forms import HistoriaClinicaForm

class HistoriaListView(ListView):
    model = HistoriaClinica
    template_name = 'historias_clinicas/listar.html'

class HistoriaCreateView(CreateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = 'form.html'
    success_url = reverse_lazy('historias:listar')

class HistoriaUpdateView(UpdateView):
    model = HistoriaClinica
    form_class = HistoriaClinicaForm
    template_name = 'form.html'
    success_url = reverse_lazy('historias:listar')

class HistoriaDeleteView(DeleteView):
    model = HistoriaClinica
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('historias:listar')
