# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_personal_relations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalrelation',
            old_name='kiNd',
            new_name='kind',
        ),
        migrations.RenameField(
            model_name='personalrelation',
            old_name='peRson',
            new_name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
