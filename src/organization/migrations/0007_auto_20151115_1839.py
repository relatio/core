# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_organization_kind'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Organization'},
        ),
        migrations.AlterModelOptions(
            name='organizationalrelation',
            options={'verbose_name': 'Organization Kind'},
        ),
        migrations.AlterModelOptions(
            name='organizationalrelationkind',
            options={'verbose_name': 'Organization Relation Kind'},
        ),
        migrations.AlterModelOptions(
            name='organizationkind',
            options={'verbose_name': 'Organization Kind'},
        ),
        migrations.AlterField(
            model_name='organization',
            name='build',
            field=models.DateField(null=True, blank=True, verbose_name='build'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='cease',
            field=models.DateField(null=True, blank=True, verbose_name='cease'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='image',
            field=models.ImageField(blank=True, verbose_name='image', upload_to=''),
        ),
        migrations.AlterField(
            model_name='organization',
            name='kind',
            field=models.ForeignKey(blank=True, to='organization.OrganizationKind', null=True, verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='metadata',
            field=django_hstore.fields.DictionaryField(blank=True, verbose_name='metadata'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='organizational_relation',
            field=models.ManyToManyField(to='organization.Organization', through='organization.OrganizationalRelation', related_name='organizational_relations', verbose_name='organization relation'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='public_name',
            field=models.CharField(verbose_name='public name', max_length=255),
        ),
        migrations.AlterField(
            model_name='organizationalrelation',
            name='kind',
            field=models.ForeignKey(to='organization.OrganizationalRelationKind', verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='organizationalrelation',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', related_name='organization_organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='organizationalrelation',
            name='relation',
            field=models.ForeignKey(to='organization.Organization', related_name='organization_related_organization', verbose_name='relation'),
        ),
        migrations.AlterField(
            model_name='organizationalrelationkind',
            name='back',
            field=models.CharField(verbose_name='back', max_length=255),
        ),
        migrations.AlterField(
            model_name='organizationalrelationkind',
            name='kind',
            field=models.CharField(verbose_name='kind', max_length=255),
        ),
        migrations.AlterField(
            model_name='organizationkind',
            name='kind',
            field=models.CharField(verbose_name='kind', max_length=255),
        ),
    ]
