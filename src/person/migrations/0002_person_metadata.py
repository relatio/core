# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.postgres.operations import HStoreExtension
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        HStoreExtension(),
        migrations.AddField(
            model_name='person',
            name='metadata',
            field=django_hstore.fields.DictionaryField(blank=True),
        ),
    ]
