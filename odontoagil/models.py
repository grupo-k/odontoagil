from datetime import date
from django.db import models

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    estado_civil = models.CharField(max_length=20, blank=True)
    rg = models.CharField(max_length=20, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    profissao = models.CharField(max_length=100, blank=True)
    nome_mae = models.CharField(max_length=200, blank=True)
    nome_pai = models.CharField(max_length=200, blank=True)
    nome_contato_familiar = models.CharField(max_length=200, blank=True)
    grau_parentesco = models.CharField(max_length=100, blank=True)
    telefone_contato_familiar = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome_completo


class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historias_clinicas')
    motivo = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    tratamento = models.TextField(blank=True)
    recomendacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"História Clínica de {self.paciente.nome_completo}"


class Tratamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Tratamento para {self.paciente.nome_completo} iniciado em {self.data_inicio}"


class Procedimento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome


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


class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome
