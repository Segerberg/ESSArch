# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0007_auto_20180416_1130'),
        ('ip', '0068_auto_20180220_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationpackage',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='information_packages', to='tags.TagStructure'),
        ),
    ]
