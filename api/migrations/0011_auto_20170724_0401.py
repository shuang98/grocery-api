# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_itemtype_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='other_names',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
