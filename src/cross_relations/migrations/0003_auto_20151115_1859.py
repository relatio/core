# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cross_relations', '0002_auto_20151115_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='entityorganizationrelation',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='end'),
        ),
        migrations.AddField(
            model_name='entityorganizationrelation',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='start'),
        ),
        migrations.AddField(
            model_name='personentityrelation',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='end'),
        ),
        migrations.AddField(
            model_name='personentityrelation',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='start'),
        ),
        migrations.AddField(
            model_name='personorganizationrelation',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='end'),
        ),
        migrations.AddField(
            model_name='personorganizationrelation',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='start'),
        ),
    ]
