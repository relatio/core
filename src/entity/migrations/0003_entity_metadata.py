# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.postgres.operations import HStoreExtension
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_auto_20151010_1024'),
    ]

    operations = [
        HStoreExtension(),
        migrations.AddField(
            model_name='entity',
            name='metadata',
            field=django_hstore.fields.DictionaryField(blank=True),
        ),
    ]
