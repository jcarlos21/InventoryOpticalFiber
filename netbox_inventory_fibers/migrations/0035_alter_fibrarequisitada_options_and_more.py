# Generated by Django 4.1.7 on 2023-03-17 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory_fibers', '0034_remove_bobina_id_privado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fibrarequisitada',
            options={'ordering': ('id',), 'verbose_name_plural': 'Fibras Requisitadas'},
        ),
        migrations.AddField(
            model_name='fibrarequisitada',
            name='id_customizado',
            field=models.CharField(default='NA', max_length=15),
        ),
    ]