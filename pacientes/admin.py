# pacientes/admin.py
from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_nascimento', 'cidade', 'estado')
    search_fields = ('nome_completo', 'cpf', 'email')
    list_filter = ('sexo', 'estado_civil', 'cidade', 'estado')
