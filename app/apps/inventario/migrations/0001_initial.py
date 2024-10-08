# Generated by Django 5.1.1 on 2024-09-27 21:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lojas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventarioFormulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('data_conclusao', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventarioItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeContagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('flag_ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('flag_ativo', models.BooleanField(default=True)),
                ('itens', models.ManyToManyField(to='lojas.grupoproduto')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('data_conclusao', models.DateTimeField(blank=True, null=True)),
                ('ultima_atualizacao', models.DateTimeField()),
                ('status', models.CharField(default='Pendente', max_length=30)),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventarios', to='lojas.lojas')),
            ],
        ),
    ]
