# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('public_name', models.CharField(max_length=510, blank=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='', blank=True)),
                ('born', models.DateField(null=True, blank=True)),
                ('died', models.DateField(null=True, blank=True)),
            ],
        ),
    ]
