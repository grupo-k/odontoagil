from django.contrib import admin
from .models import Servico, CodigoServ, CodigoServicosSecundario

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('codigo_servicos', 'descricao_servicos', 'data_inclusao', 'material_usado', 'aparelho_apoio')
    search_fields = ('codigo_servicos', 'descricao_servicos', 'material_usado')
    list_filter = ('data_inclusao',)
    actions_on_bottom = True
    actions_on_top = False

@admin.register(CodigoServ)
class CodigoServAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    actions_on_bottom = True
    actions_on_top = False
    
    

@admin.register(CodigoServicosSecundario)
class CodigoServicosSecundarioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    actions_on_bottom = True
    actions_on_top = False
