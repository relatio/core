# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0005_auto_20151012_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='kind',
        ),
    ]
