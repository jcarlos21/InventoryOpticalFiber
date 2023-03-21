from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel

from django.urls import reverse

from django.utils import timezone

import datetime


class Fornecedor(NetBoxModel):
    nome_fornecedor = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    telefone = models.PositiveIntegerField(unique=True)
    endereco_site = models.CharField(max_length=60, unique=True)
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
    descricao = models.CharField(max_length=20, unique=True)
    comments = models.TextField(blank=True)
    class Meta:
        ordering = ('id',)
        verbose_name = 'Status'
    def __str__(self):
        return self.descricao
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:tipobobina', args=[self.pk])
    

class QuantidadeFibraCabo(NetBoxModel):
    quantidade = models.CharField(max_length=5, help_text='Entre com a quantidade de fibras no cabo. Ex.: 36FO', unique=True)
    comments = models.TextField(blank=True)
    class Meta:
        ordering = ('id',)
        verbose_name = 'Quantidade de Fibra'
    def __str__(self):
        return self.quantidade
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:quantidadefibracabo', args=[self.pk])


class Bobina(NetBoxModel):
    special_id = models.CharField(max_length=255, null=True, default=None, unique=True)
    nome_fornecedor = models.ForeignKey(to=Fornecedor, on_delete=models.PROTECT, related_name='bobinas_to_fornecedor')
    quantidade_fibras = models.ForeignKey(to=QuantidadeFibraCabo, on_delete=models.PROTECT, related_name='bobinas_to_quantidade')
    modelo = models.CharField(max_length=60)
    tipo_bobina = models.ForeignKey(to=TipoBobina, on_delete=models.PROTECT, related_name='bobinas')
    lote_cabo = models.CharField(max_length=50)
    metragem_inicial = models.FloatField(default=0)  # remover
    metragem_final = models.FloatField(default=0)  # remover
    metragem_cadastrada = models.FloatField(default=0, editable=False)
    total_estoque = models.FloatField(default=0)  # Foi necessáro colocar o default para a migration ser concluida.
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Bobinas'
    
    def __str__(self):
        return self.special_id
    
    def get_computed(self):
        self.metragem_cadastrada = self.metragem_final - self.metragem_inicial
        return self.metragem_cadastrada
    
    def save(self, *args, **kwargs):
        self.total_estoque = self.get_computed()
        
        if not self.special_id:           
           prefix = '{}'.format(timezone.now().strftime('%y'))
           prev_instances = self.__class__.objects.filter(special_id__contains=prefix)
           if prev_instances.exists():
              last_instance_id = prev_instances.last().special_id[1:5]
            #   print(last_instance_id)
              self.special_id = 'B{0:04d}_'.format(int(last_instance_id)+1)+prefix
           else:
               self.special_id = 'B{0:04d}_'.format(1)+prefix
        super(Bobina, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:bobina', args=[self.pk])


class Requisicao(NetBoxModel):
    ordem_de_servico = models.CharField(max_length=15, unique=True)
    imagem_OS = models.FileField(upload_to='uploads/OS', unique=True)
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Ordens de Serviço'
    def __str__(self):
        return self.ordem_de_servico
    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:requisicao', args=[self.pk])


class FibraRequisitada(NetBoxModel):
    id_customizado = models.CharField(max_length=255, null=True, default=None, unique=True, editable=False)
    bobina = models.ForeignKey(to=Bobina, on_delete=models.PROTECT)
    metragem_requisitada = models.FloatField(default=0)
    # file will be uploaded to MEDIA_ROOT/uploads
    imagem_corte_cabo = models.ImageField(upload_to='uploads/cortes', unique=True)
    ordem_de_servico = models.ForeignKey(to=Requisicao, on_delete=models.PROTECT, related_name='fibrarequisitada_to_ordem_servico')  # related_name='fibrarequisitada_to_ordem_servico'
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Fibras Requisitadas'
    def __str__(self):
        return self.id_customizado
        
    def save(self, *args, **kwargs):

        # Bobina.objects.filter(special_id=self.bobina).update(total_estoque = (Bobina.total_estoque - self.metragem_requisitada))
        Bobina.objects.filter(special_id=self.bobina).update(total_estoque = self.metragem_requisitada)

        total = Bobina.objects.filter(special_id=self.bobina).values('total_estoque')
        print(f'Estou aqui: {total}' )

        if not self.id_customizado:           
           prefix = '{}'.format(timezone.now().strftime('%y'))
           prev_instances = self.__class__.objects.filter(id_customizado__contains=prefix)
           if prev_instances.exists():
              last_instance_id = prev_instances.last().id_customizado[3:7]
              self.id_customizado = 'REQ{0:04d}_'.format(int(last_instance_id)+1)+prefix
           else:
               self.id_customizado = 'REQ{0:04d}_'.format(1)+prefix
               
        super(FibraRequisitada, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('plugins:netbox_inventory_fibers:fibrarequisitada', args=[self.pk])

