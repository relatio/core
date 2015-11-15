# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cross_relations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entityorganizationrelation',
            options={'verbose_name': 'Entity Organization Relation'},
        ),
        migrations.AlterModelOptions(
            name='personentityrelation',
            options={'verbose_name': 'Person Entity Relation'},
        ),
        migrations.AlterModelOptions(
            name='personorganizationrelation',
            options={'verbose_name': 'Person Organization Relation'},
        ),
        migrations.AlterField(
            model_name='entityorganizationrelation',
            name='entity',
            field=models.ForeignKey(to='entity.Entity', related_name='entity_organization_entity', verbose_name='entity'),
        ),
        migrations.AlterField(
            model_name='entityorganizationrelation',
            name='kind',
            field=models.ForeignKey(to='cross_relations.EntityOrganizationRelationKind', verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='entityorganizationrelation',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', related_name='entity_organization_organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='entityorganizationrelationkind',
            name='back',
            field=models.CharField(verbose_name='back', max_length=255),
        ),
        migrations.AlterField(
            model_name='entityorganizationrelationkind',
            name='kind',
            field=models.CharField(verbose_name='kind', max_length=255),
        ),
        migrations.AlterField(
            model_name='personentityrelation',
            name='entity',
            field=models.ForeignKey(to='entity.Entity', related_name='person_entity_entity', verbose_name='entity'),
        ),
        migrations.AlterField(
            model_name='personentityrelation',
            name='kind',
            field=models.ForeignKey(to='cross_relations.PersonEntityRelationKind', verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='personentityrelation',
            name='person',
            field=models.ForeignKey(to='person.Person', related_name='person_entity_person', verbose_name='person'),
        ),
        migrations.AlterField(
            model_name='personentityrelationkind',
            name='back',
            field=models.CharField(verbose_name='back', max_length=255),
        ),
        migrations.AlterField(
            model_name='personentityrelationkind',
            name='kind',
            field=models.CharField(verbose_name='kind', max_length=255),
        ),
        migrations.AlterField(
            model_name='personorganizationrelation',
            name='kind',
            field=models.ForeignKey(to='cross_relations.PersonOrganizationRelationKind', verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='personorganizationrelation',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', related_name='person_organization_organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='personorganizationrelation',
            name='person',
            field=models.ForeignKey(to='person.Person', related_name='person_organization_person', verbose_name='person'),
        ),
        migrations.AlterField(
            model_name='personorganizationrelationkind',
            name='back',
            field=models.CharField(verbose_name='back', max_length=255),
        ),
        migrations.AlterField(
            model_name='personorganizationrelationkind',
            name='kind',
            field=models.CharField(verbose_name='kind', max_length=255),
        ),
    ]
