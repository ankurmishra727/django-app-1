# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20171116_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfile',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
