# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_auto_20151115_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalrelation',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='end'),
        ),
        migrations.AddField(
            model_name='personalrelation',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='start'),
        ),
    ]
