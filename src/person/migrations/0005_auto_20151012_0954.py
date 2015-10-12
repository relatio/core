# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0005_auto_20151012_0954'),
        ('cross_relations', '0001_initial'),
        ('organization', '0005_auto_20151012_0954'),
        ('person', '0004_auto_20151012_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_entity_relation',
            field=models.ManyToManyField(to='entity.Entity', through='cross_relations.PersonEntityRelation', related_name='person_entity_relations'),
        ),
        migrations.AddField(
            model_name='person',
            name='person_organization_relation',
            field=models.ManyToManyField(to='organization.Organization', through='cross_relations.PersonOrganizationRelation', related_name='person_organization_relations'),
        ),
        migrations.AlterField(
            model_name='personalrelation',
            name='person',
            field=models.ForeignKey(to='person.Person', related_name='person_person'),
        ),
        migrations.AlterField(
            model_name='personalrelation',
            name='relation',
            field=models.ForeignKey(to='person.Person', related_name='peson_related_person'),
        ),
    ]
