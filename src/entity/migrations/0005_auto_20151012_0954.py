# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cross_relations', '0001_initial'),
        ('entity', '0004_auto_20151012_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='entity_organization_relation',
            field=models.ManyToManyField(to='entity.Entity', through='cross_relations.EntityOrganizationRelation', related_name='entity_organization_relations'),
        ),
        migrations.AlterField(
            model_name='entityrelation',
            name='entity',
            field=models.ForeignKey(to='entity.Entity', related_name='entity_entity'),
        ),
        migrations.AlterField(
            model_name='entityrelation',
            name='relation',
            field=models.ForeignKey(to='entity.Entity', related_name='entity_related_entity'),
        ),
    ]
