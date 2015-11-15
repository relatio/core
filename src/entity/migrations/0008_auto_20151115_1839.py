# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0007_entity_kind'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name': 'Entity'},
        ),
        migrations.AlterModelOptions(
            name='entitykind',
            options={'verbose_name': 'Entity Kind'},
        ),
        migrations.AlterModelOptions(
            name='entityrelation',
            options={'verbose_name': 'Entity Relation'},
        ),
        migrations.AlterModelOptions(
            name='entityrelationkind',
            options={'verbose_name': 'Entity Relation Kind'},
        ),
        migrations.AlterField(
            model_name='entity',
            name='build',
            field=models.DateField(null=True, blank=True, verbose_name='build'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='cease',
            field=models.DateField(null=True, blank=True, verbose_name='cease'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='entity_organization_relation',
            field=models.ManyToManyField(to='entity.Entity', through='cross_relations.EntityOrganizationRelation', related_name='entity_organization_relations', verbose_name='entity organization relation'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='entity_relation',
            field=models.ManyToManyField(to='entity.Entity', through='entity.EntityRelation', related_name='entity_relations', verbose_name='entity relation'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='image',
            field=models.ImageField(blank=True, verbose_name='image', upload_to=''),
        ),
        migrations.AlterField(
            model_name='entity',
            name='kind',
            field=models.ForeignKey(blank=True, to='entity.EntityKind', null=True, verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='metadata',
            field=django_hstore.fields.DictionaryField(blank=True, verbose_name='metadata'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='official_id',
            field=models.CharField(blank=True, verbose_name='official id', max_length=255),
        ),
        migrations.AlterField(
            model_name='entity',
            name='official_name',
            field=models.CharField(blank=True, verbose_name='official name', max_length=255),
        ),
        migrations.AlterField(
            model_name='entity',
            name='public_name',
            field=models.CharField(verbose_name='public name', max_length=255),
        ),
        migrations.AlterField(
            model_name='entitykind',
            name='kind',
            field=models.CharField(verbose_name='kind', max_length=255),
        ),
        migrations.AlterField(
            model_name='entityrelation',
            name='entity',
            field=models.ForeignKey(to='entity.Entity', related_name='entity_entity', verbose_name='entity'),
        ),
        migrations.AlterField(
            model_name='entityrelation',
            name='kind',
            field=models.ForeignKey(to='entity.EntityRelationKind', verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='entityrelation',
            name='metadata',
            field=django_hstore.fields.DictionaryField(blank=True, verbose_name='metadata'),
        ),
        migrations.AlterField(
            model_name='entityrelation',
            name='relation',
            field=models.ForeignKey(to='entity.Entity', related_name='entity_related_entity', verbose_name='relation'),
        ),
        migrations.AlterField(
            model_name='entityrelationkind',
            name='back',
            field=models.CharField(verbose_name='back', max_length=255),
        ),
        migrations.AlterField(
            model_name='entityrelationkind',
            name='kind',
            field=models.CharField(verbose_name='kind', max_length=255),
        ),
    ]
