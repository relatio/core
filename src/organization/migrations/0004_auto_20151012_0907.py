# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_organization_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationalRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metadata', django_hstore.fields.DictionaryField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationalRelationKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(max_length=255)),
                ('back', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='organizationalrelation',
            name='kind',
            field=models.ForeignKey(to='organization.OrganizationalRelationKind'),
        ),
        migrations.AddField(
            model_name='organizationalrelation',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', related_name='organization'),
        ),
        migrations.AddField(
            model_name='organizationalrelation',
            name='relation',
            field=models.ForeignKey(to='organization.Organization', related_name='related_organization'),
        ),
        migrations.AddField(
            model_name='organization',
            name='organizational_relation',
            field=models.ManyToManyField(to='organization.Organization', related_name='organizational_relations', through='organization.OrganizationalRelation'),
        ),
    ]
