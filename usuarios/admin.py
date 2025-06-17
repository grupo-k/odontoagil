# usuarios/admin.py
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cargo')
    search_fields = ('nome', 'email', 'cargo')
    list_filter = ('cargo',)
