# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
