# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20170729_0551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onsaleitem',
            old_name='full_price',
            new_name='discount',
        ),
    ]
