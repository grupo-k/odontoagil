from django import forms
from .models import HistoriaClinica

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = '__all__'
        widgets = {
            'data_criacao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
