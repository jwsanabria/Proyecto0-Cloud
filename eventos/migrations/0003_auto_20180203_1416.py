# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-02-03 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_fec_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fec_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
