# Generated by Django 4.1.7 on 2023-03-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory_fibers', '0032_bobina_id_privado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bobina',
            name='id_privado',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
