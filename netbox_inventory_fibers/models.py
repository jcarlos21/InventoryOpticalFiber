from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel

from django.contrib.auth import get_user_model
User=get_user_model()


class Fornecedor(NetBoxModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    nome_fornecedor = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefone = models.PositiveIntegerField()
    endereco_site = models.CharField(max_length=60)
    
    class Meta:
        ordering = ('nome_fornecedor',)
    
    def __str__(self):
        return self.nome_fornecedor


class TipoBobina(NetBoxModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=20)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.id


class Bobina(NetBoxModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    nome_fornecedor = models.ForeignKey(to=Fornecedor, on_delete=models.PROTECT)
    quantidade_fibras = models.IntegerField()
    descricao = models.CharField(max_length=60)
    tipo_bobina = models.ForeignKey(to=TipoBobina, on_delete=models.PROTECT)
    lote_cabo = models.CharField(max_length=50)
    metragem_inicial = models.FloatField()
    metragem_final = models.FloatField()
    total_metragem = models.FloatField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.id

    def restante(self):
        self.total_metragem = self.metragem_final - self.metragem_inicial


class Requisicao(NetBoxModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    metragem_requisitada = models.FloatField()
    # data_requisicao = models.DateField(auto_now=True)  Não necessário, pois o atribuito 'created' já é criado por padrão
    bilhete_associado = models.CharField(max_length=15)

    class Meta:
        ordering = ('id',)
    
    def __str__(self):
        return self.id


class FibraRequisitada(NetBoxModel):
    bobina = models.ForeignKey(to=Bobina, on_delete=models.PROTECT)
    requisicao = models.ForeignKey(to=Requisicao, on_delete=models.PROTECT)
    # file will be uploaded to MEDIA_ROOT/uploads
    imagem_corte_cabo = models.FileField(upload_to='uploads/')

    class Meta:
        ordering = ('id',)
    
    def __str__(self):
        return self.id
