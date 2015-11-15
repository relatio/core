# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0008_auto_20151115_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='address',
            field=models.CharField(blank=True, verbose_name='address', max_length=1000),
        ),
        migrations.AddField(
            model_name='entity',
            name='email',
            field=models.EmailField(blank=True, verbose_name='email 1', max_length=254),
        ),
        migrations.AddField(
            model_name='entity',
            name='facebook',
            field=models.CharField(blank=True, verbose_name='facebook', max_length=1000),
        ),
        migrations.AddField(
            model_name='entity',
            name='id_card_number',
            field=models.CharField(blank=True, verbose_name='id card number', max_length=1000),
        ),
        migrations.AddField(
            model_name='entity',
            name='instagram',
            field=models.CharField(blank=True, verbose_name='instagram', max_length=1000),
        ),
        migrations.AddField(
            model_name='entity',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, verbose_name='phone 1', max_length=128),
        ),
        migrations.AddField(
            model_name='entity',
            name='social_security_number',
            field=models.CharField(blank=True, verbose_name='social security number', max_length=1000),
        ),
        migrations.AddField(
            model_name='entity',
            name='twitter',
            field=models.CharField(blank=True, verbose_name='twitter', max_length=1000),
        ),
        migrations.AddField(
            model_name='entity',
            name='webpage',
            field=models.CharField(blank=True, verbose_name='webpage', max_length=1000),
        ),
        migrations.AddField(
            model_name='entityrelation',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='end'),
        ),
        migrations.AddField(
            model_name='entityrelation',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='start'),
        ),
    ]
