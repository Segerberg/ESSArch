# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0058_auto_20171128_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='workarea',
            name='successfully_validated',
            field=jsonfield.fields.JSONField(default=None, null=True),
        ),
    ]
