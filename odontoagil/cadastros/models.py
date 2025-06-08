from django.db import models

class CodigoServ(models.Model):
    nome = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

class CodigoServicosSecundario(models.Model):
    nome = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

def get_codigo_servicos_choices():
    return [(c.nome, c.nome) for c in CodigoServ.objects.all()]

def get_codigo_servicos_secundarios_choices():
    return [(c.nome, c.nome) for c in CodigoServicosSecundario.objects.all()]

class Servico(models.Model):
    data_inclusao = models.DateField()
    codigo_servicos = models.CharField(max_length=50, choices=get_codigo_servicos_choices)
    material_usado = models.CharField(max_length=255)
    descricao_servicos = models.TextField(blank=True, null=True)
    codigo_servicos_secundarios = models.CharField(max_length=50, choices=get_codigo_servicos_secundarios_choices, blank=True, null=True)
    descricao_servicos_secundarios = models.TextField(blank=True, null=True)
    aparelho_apoio = models.CharField(max_length=255)
    observacoes = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='img/servicos', null=True, blank=True)

    def __str__(self):
        return f"{self.codigo_servicos} - {self.descricao_servicos}"

