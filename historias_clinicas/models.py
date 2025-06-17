from django.db import models
from pacientes.models import Paciente

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='historias_clinicas'
    )
    motivo = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    tratamento = models.TextField(blank=True)
    recomendacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"História Clínica de {self.paciente.nome_completo}"
