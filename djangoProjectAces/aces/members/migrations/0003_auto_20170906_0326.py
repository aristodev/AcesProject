# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20170906_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
