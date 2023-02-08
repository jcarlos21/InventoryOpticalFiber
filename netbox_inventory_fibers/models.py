from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel

from django.conf import settings

from utilities.choices import ChoiceSet


class StatusChoices(ChoiceSet):
    key = 'Bobina.descricao'

    CHOICES = [
        ('disponível', 'Disponível', 'green'),
        ('sem estoque', 'Sem estoque', 'red'),
        ('quase no fim', 'Quase no fim', 'orange'),
    ]


# class Usuario(NetBoxModel):
#     codUsuario = models.BigAutoField(primary_key=True)
#     nomeUsuario = models.CharField(max_length=100)
#     cpfUsuario = models.CharField(max_length=11)
#     senha = models.CharField(max_length=15)
#     nivelPermissao = models.PositiveIntegerField(max_length=1)

#     def __str__(self):
#         return self.nomeUsuario

# class Fornecedor(NetBoxModel, models.Model):
#     codFornecedor = models.BigAutoField(primary_key=True)
#     nomeFornecedor = models.CharField(max_length=80)
#     email = models.CharField(max_length=50)
#     telefone = models.CharField(max_length=11)
#     enderecoEletronico = NetBoxModel.CharField(max_length=30)
    
#     author = models.ForeignKey(
#         settings.AUTO_USER_MODEL,
#         on_delete=models.CASCADE,
#     )

class Bobina(NetBoxModel):
    codBobina = models.BigAutoField(primary_key=True)
    codBobinaAno = models.CharField(max_length=9)
    quantidadeFibras = models.IntegerField()
    descricao = models.CharField(max_length=50)
    # statusBobina = models.CharField(max_length=30)
    # TipoBobina = models.ForeignKey(
    #     to=TipoBobina,
    #     on_delete=models.CASCADE,
    #     related_name='StatusBobina'
    # )

    def get_default_action_color(self):
        return StatusChoices.colors.get(self.descricao)
    
    def __str__(self):
        return self.codBobinaAno



# class TipoBobina(NetBoxModel):