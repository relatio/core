# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_name', models.CharField(max_length=255)),
                ('official_name', models.CharField(max_length=255, blank=True)),
                ('official_id', models.CharField(max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('build', models.DateField(blank=True, null=True)),
                ('cease', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
