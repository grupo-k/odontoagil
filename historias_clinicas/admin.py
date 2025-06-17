# historias_clinicas/admin.py
from django.contrib import admin
from .models import HistoriaClinica

@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data_criacao', 'diagnostico')
    search_fields = ('paciente__nome_completo', 'diagnostico', 'motivo')
    list_filter = ('data_criacao',)
    autocomplete_fields = ['paciente']
