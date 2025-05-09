# Generated by Django 5.2 on 2025-04-15 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dentistas', '0001_initial'),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('anotacoes', models.TextField(blank=True, null=True)),
                ('dentista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prontuarios', to='dentistas.dentista')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prontuarios', to='pacientes.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemProntuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='prontuarios/')),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
                ('prontuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='prontuarios.prontuario')),
            ],
        ),
    ]
