# Generated by Django 4.1.6 on 2023-02-08 00:30

from django.db import migrations, models
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0084_staging'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bobina',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('codBobina', models.BigAutoField(primary_key=True, serialize=False)),
                ('codBobinaAno', models.CharField(max_length=9)),
                ('quantidadeFibras', models.IntegerField(max_length=2)),
                ('descricao', models.CharField(max_length=50)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]