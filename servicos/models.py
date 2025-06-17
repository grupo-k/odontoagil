from django.db import models
from usuarios.models import Usuario

class Servico(models.Model):
    data_inclusao = models.DateField()
    codigo_servicos = models.CharField(max_length=100)
    material_usado = models.CharField(max_length=255)
    descricao_servicos = models.TextField()
    codigo_servicos_secundario = models.CharField(max_length=100, blank=True, null=True)
    descricao_servicos_secundario = models.TextField(blank=True, null=True)
    aparelho_apoio = models.CharField(max_length=255, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.descricao_servicos

class Atendimento(models.Model):
    paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.CASCADE)
    servico = models.ForeignKey('servicos.Servico', on_delete=models.CASCADE)
    profissional = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    data_atendimento = models.DateTimeField()

    def __str__(self):
        return f"{self.servico} - {self.paciente.nome_completo} em {self.data_atendimento.date()}"