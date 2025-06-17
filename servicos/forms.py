from django import forms
from .models import Servico, Atendimento

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            'data_inclusao': forms.DateInput(attrs={'type': 'date'}),
        }

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = '__all__'
        widgets = {
            'data_atendimento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
