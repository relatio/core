# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0003_entity_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EntityRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metadata', django_hstore.fields.DictionaryField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityRelationKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(max_length=255)),
                ('back', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='entity',
            name='kind',
            field=models.CharField(max_length=255, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entityrelation',
            name='entity',
            field=models.ForeignKey(to='entity.Entity', related_name='entity'),
        ),
        migrations.AddField(
            model_name='entityrelation',
            name='kind',
            field=models.ForeignKey(to='entity.EntityRelationKind'),
        ),
        migrations.AddField(
            model_name='entityrelation',
            name='relation',
            field=models.ForeignKey(to='entity.Entity', related_name='related_entity'),
        ),
        migrations.AddField(
            model_name='entity',
            name='entity_relation',
            field=models.ManyToManyField(to='entity.Entity', related_name='entity_relations', through='entity.EntityRelation'),
        ),
    ]
