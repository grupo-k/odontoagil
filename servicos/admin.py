# servicos/admin.py
from django.contrib import admin
from .models import Servico, Atendimento

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('codigo_servicos', 'descricao_servicos', 'data_inclusao')
    search_fields = ('codigo_servicos', 'descricao_servicos', 'material_usado')
    list_filter = ('data_inclusao',)

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'profissional', 'servico', 'data_atendimento')
    search_fields = ('paciente__nome_completo', 'profissional__nome', 'servico__descricao_servicos')
    list_filter = ('data_atendimento',)
    autocomplete_fields = ['paciente', 'profissional', 'servico']
