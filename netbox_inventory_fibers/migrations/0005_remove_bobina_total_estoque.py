# Generated by Django 4.1.7 on 2023-02-26 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_inventory_fibers', '0004_alter_bobina_total_estoque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bobina',
            name='total_estoque',
        ),
    ]