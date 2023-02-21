from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel

from django.contrib.auth import get_user_model
User=get_user_model()


class Fornecedor(NetBoxModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    nome_fornecedor = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.PositiveIntegerField()
    endereco_site = models.CharField(max_length=60)
    
    class Meta:
        ordering = ('nome_fornecedor',)
    
    def __str__(self):
        return self.nome_fornecedor

class TipoBobina(NetBoxModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=20)


class Bobina(NetBoxModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    nome_fornecedor = models.ForeignKey(to=Fornecedor, on_delete=models.PROTECT)
    quantidade_fibras = models.PositiveIntegerField()
    descricao = models.CharField(max_length=60)
    tipo_bobina = models.ForeignKey(to=TipoBobina, on_delete=models.PROTECT)
    
