# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-31 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_auto_20180129_0448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appraisaljob',
            options={'permissions': (('run_appraisaljob', 'Can run appraisal job'),)},
        ),
    ]