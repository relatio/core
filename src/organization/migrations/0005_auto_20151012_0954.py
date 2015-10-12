# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20151012_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationalrelation',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', related_name='organization_organization'),
        ),
        migrations.AlterField(
            model_name='organizationalrelation',
            name='relation',
            field=models.ForeignKey(to='organization.Organization', related_name='organization_related_organization'),
        ),
    ]
