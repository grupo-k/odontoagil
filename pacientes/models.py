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
