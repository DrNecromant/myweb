# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-01 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_usericon'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='label',
            field=models.CharField(blank=True, max_length=4, null=True, unique=True),
        ),
    ]
