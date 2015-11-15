# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20151012_1007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person'},
        ),
        migrations.AlterModelOptions(
            name='personalrelation',
            options={'verbose_name': 'Person Relation'},
        ),
        migrations.AlterModelOptions(
            name='personalrelationkind',
            options={'verbose_name': 'Person Relation Kind'},
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, verbose_name='address', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='email_1',
            field=models.EmailField(blank=True, verbose_name='email 1', max_length=254),
        ),
        migrations.AddField(
            model_name='person',
            name='email_2',
            field=models.EmailField(blank=True, verbose_name='email 2', max_length=254),
        ),
        migrations.AddField(
            model_name='person',
            name='facebook',
            field=models.CharField(blank=True, verbose_name='facebook', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='id_card_number',
            field=models.CharField(blank=True, verbose_name='id card number', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='instagram',
            field=models.CharField(blank=True, verbose_name='instagram', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='phone_1',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, verbose_name='phone 1', max_length=128),
        ),
        migrations.AddField(
            model_name='person',
            name='phone_2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, verbose_name='phone 2', max_length=128),
        ),
        migrations.AddField(
            model_name='person',
            name='social_security_number',
            field=models.CharField(blank=True, verbose_name='social security number', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='twitter',
            field=models.CharField(blank=True, verbose_name='twitter', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='webpage',
            field=models.CharField(blank=True, verbose_name='webpage', max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='born',
            field=models.DateField(blank=True, null=True, verbose_name='born'),
        ),
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='person',
            name='died',
            field=models.DateField(blank=True, null=True, verbose_name='died'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(verbose_name='first name', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, verbose_name='image', upload_to=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(verbose_name='last name', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='metadata',
            field=django_hstore.fields.DictionaryField(blank=True, verbose_name='metadata'),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_entity_relation',
            field=models.ManyToManyField(to='entity.Entity', through='cross_relations.PersonEntityRelation', related_name='person_entity_relations', verbose_name='personal entity relation'),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_organization_relation',
            field=models.ManyToManyField(to='organization.Organization', through='cross_relations.PersonOrganizationRelation', related_name='person_organization_relations', verbose_name='personal organization relation'),
        ),
        migrations.AlterField(
            model_name='person',
            name='personal_relation',
            field=models.ManyToManyField(to='person.Person', through='person.PersonalRelation', related_name='personal_relations', verbose_name='personal relation'),
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(blank=True, verbose_name='position', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='public_name',
            field=models.CharField(blank=True, verbose_name='public name', max_length=510),
        ),
        migrations.AlterField(
            model_name='personalrelation',
            name='kind',
            field=models.ForeignKey(to='person.PersonalRelationKind', verbose_name='kind'),
        ),
        migrations.AlterField(
            model_name='personalrelation',
            name='metadata',
            field=django_hstore.fields.DictionaryField(blank=True, verbose_name='metadata'),
        ),
        migrations.AlterField(
            model_name='personalrelation',
            name='person',
            field=models.ForeignKey(to='person.Person', related_name='person_person', verbose_name='person'),
        ),
        migrations.AlterField(
            model_name='personalrelation',
            name='relation',
            field=models.ForeignKey(to='person.Person', related_name='peson_related_person', verbose_name='relation'),
        ),
        migrations.AlterField(
            model_name='personalrelationkind',
            name='back',
            field=models.CharField(verbose_name='back', max_length=255),
        ),
        migrations.AlterField(
            model_name='personalrelationkind',
            name='kind',
            field=models.CharField(verbose_name='kind', max_length=255),
        ),
    ]
