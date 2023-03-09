from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel

from django.urls import reverse

# from django.contrib.auth import get_user_model
# User=get_user_model()


class Fornecedor(NetBoxModel):
    # author = models.ForeignKey(User, on_delete=models.PROTECT)
    nome_fornecedor = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefone = models.PositiveIntegerField()
    endereco_site = models.CharField(max_length=60)
    comments = models.TextField(blank=True)
    class Meta:
        ordering = ('nome_fornecedor',)
        # verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
    def __str__(self):
        return self.nome_fornecedor
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:fornecedor', args=[self.pk])


class TipoBobina(NetBoxModel):
    # author = models.ForeignKey(User, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=20)
    comments = models.TextField(blank=True)
    class Meta:
        ordering = ('id',)
        verbose_name = 'Tipos de Bobina'
    def __str__(self):
        return self.descricao
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:tipobobina', args=[self.pk])
    

class QuantidadeFibraCabo(NetBoxModel):
    quantidade = models.CharField(max_length=5, help_text='Entre com a quantidade de fibras no cabo. Ex.: 36FO')
    comments = models.TextField(blank=True)
    class Meta:
        ordering = ('id',)
        verbose_name = 'Quantidade de Fibra'
    def __str__(self):
        return self.quantidade
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:quantidadefibracabo', args=[self.pk])


class Bobina(NetBoxModel):
    # author = models.ForeignKey(User, on_delete=models.PROTECT)
    nome_fornecedor = models.ForeignKey(to=Fornecedor, on_delete=models.PROTECT, related_name='bobinas_to_fornecedor')
    # quantidade_fibras = models.IntegerField()
    quantidade_fibras = models.ForeignKey(to=QuantidadeFibraCabo, on_delete=models.PROTECT, related_name='bobinas_to_quantidade')
    modelo = models.CharField(max_length=60)
    tipo_bobina = models.ForeignKey(to=TipoBobina, on_delete=models.PROTECT, related_name='bobinas')
    lote_cabo = models.CharField(max_length=50)
    metragem_inicial = models.FloatField()
    metragem_final = models.FloatField()
    total_metragem = models.FloatField()
    total_estoque = models.FloatField(default=0)  # Foi necessáro colocar o default para a migration ser concluida.
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Bobinas'
    def __str__(self):
        return self.modelo
    def restante(self):
        self.total_metragem = self.metragem_final - self.metragem_inicial
        # self.total_estoque = self.total_metragem
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:bobina', args=[self.pk])


class Requisicao(NetBoxModel):
    # author = models.ForeignKey(User, on_delete=models.PROTECT)
    ordem_de_servico = models.CharField(max_length=15)
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Requisições'
    def __str__(self):
        return self.ordem_de_servico
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:requisicao', args=[self.pk])


class FibraRequisitada(NetBoxModel):
    bobina = models.ForeignKey(to=Bobina, on_delete=models.PROTECT)
    metragem_requisitada = models.FloatField(default=0)  # Foi necessáro colocar o default para a migration ser concluida.
    # file will be uploaded to MEDIA_ROOT/uploads
    imagem_corte_cabo = models.FileField(upload_to='uploads/')
    ordem_de_servico = models.ForeignKey(to=Requisicao, on_delete=models.PROTECT)  # related_name='fibrarequisitada_to_ordem_servico'
    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.id

