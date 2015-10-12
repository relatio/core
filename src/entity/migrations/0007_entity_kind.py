# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0006_remove_entity_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, to='entity.EntityKind'),
        ),
    ]
