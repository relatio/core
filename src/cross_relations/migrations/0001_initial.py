# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0004_auto_20151012_0907'),
        ('organization', '0005_auto_20151012_0954'),
        ('person', '0004_auto_20151012_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityOrganizationRelation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('metadata', django_hstore.fields.DictionaryField(blank=True)),
                ('entity', models.ForeignKey(to='entity.Entity', related_name='entity_organization_entity')),
            ],
        ),
        migrations.CreateModel(
            name='EntityOrganizationRelationKind',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('back', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonEntityRelation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('metadata', django_hstore.fields.DictionaryField(blank=True)),
                ('entity', models.ForeignKey(to='entity.Entity', related_name='person_entity_entity')),
            ],
        ),
        migrations.CreateModel(
            name='PersonEntityRelationKind',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('back', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonOrganizationRelation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('metadata', django_hstore.fields.DictionaryField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonOrganizationRelationKind',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('back', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='personorganizationrelation',
            name='kind',
            field=models.ForeignKey(to='cross_relations.PersonOrganizationRelationKind'),
        ),
        migrations.AddField(
            model_name='personorganizationrelation',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', related_name='person_organization_organization'),
        ),
        migrations.AddField(
            model_name='personorganizationrelation',
            name='person',
            field=models.ForeignKey(to='person.Person', related_name='person_organization_person'),
        ),
        migrations.AddField(
            model_name='personentityrelation',
            name='kind',
            field=models.ForeignKey(to='cross_relations.PersonEntityRelationKind'),
        ),
        migrations.AddField(
            model_name='personentityrelation',
            name='person',
            field=models.ForeignKey(to='person.Person', related_name='person_entity_person'),
        ),
        migrations.AddField(
            model_name='entityorganizationrelation',
            name='kind',
            field=models.ForeignKey(to='cross_relations.EntityOrganizationRelationKind'),
        ),
        migrations.AddField(
            model_name='entityorganizationrelation',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', related_name='entity_organization_organization'),
        ),
    ]
