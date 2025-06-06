#        fields = '__all__'
from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['codigo_servicos', 'material_usado', 'descricao_servicos', 
                'codigo_servicos_secundarios', 'descricao_servicos_secundarios', 
                'aparelho_apoio', 'observacoes', 'foto']
        
