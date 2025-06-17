from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Servico, Atendimento
from .forms import ServicoForm, AtendimentoForm

class ServicoListView(ListView):
    model = Servico
    template_name = 'servicos/listar.html'

class ServicoCreateView(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'form.html'
    success_url = reverse_lazy('servicos:listar')

class ServicoUpdateView(UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'form.html'
    success_url = reverse_lazy('servicos:listar')

class ServicoDeleteView(DeleteView):
    model = Servico
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('servicos:listar')

# Atendimento
class AtendimentoListView(ListView):
    model = Atendimento
    template_name = 'servicos/atendimentos/listar.html'
    context_object_name = 'atendimentos'

class AtendimentoCreateView(CreateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'form.html'
    success_url = reverse_lazy('servicos:atendimentos_listar')
