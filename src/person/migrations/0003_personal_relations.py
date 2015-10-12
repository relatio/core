# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_person_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('metadata', django_hstore.fields.DictionaryField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalRelationKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('kind', models.CharField(max_length=255)),
                ('back', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='personalrelation',
            name='kiNd',
            field=models.ForeignKey(to='person.PersonalRelationKind'),
        ),
        migrations.AddField(
            model_name='personalrelation',
            name='peRson',
            field=models.ForeignKey(related_name='person', to='person.Person'),
        ),
        migrations.AddField(
            model_name='personalrelation',
            name='relation',
            field=models.ForeignKey(related_name='related_person', to='person.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='personal_relation',
            field=models.ManyToManyField(to='person.Person', related_name='personal_relations', through='person.PersonalRelation'),
        ),
    ]
