# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20151012_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='kind',
            field=models.ForeignKey(null=True, to='organization.OrganizationKind', blank=True),
        ),
    ]
