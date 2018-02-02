# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-02-01 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_evento', models.CharField(help_text='Nombre del evento', max_length=200, verbose_name='Nombre')),
                ('ind_categoria', models.CharField(choices=[('CONF', 'Conferencia'), ('SEMI', 'Seminario'), ('CONG', 'Congreso'), ('CURS', 'Curso')], max_length=4)),
                ('txt_lugar', models.CharField(help_text='Lugar', max_length=100, verbose_name='Lugar')),
                ('txt_direccion', models.CharField(help_text='Dirección', max_length=100, verbose_name='Dirección')),
                ('fec_inicio', models.DateField(help_text='Fecha de inicio')),
                ('fec_final', models.DateField(help_text='Fecha de final')),
                ('ind_modalidad', models.CharField(choices=[('P', 'Presencial'), ('V', 'Virtual')], max_length=1)),
            ],
        ),
    ]
