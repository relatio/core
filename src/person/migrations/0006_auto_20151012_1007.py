# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20151012_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
