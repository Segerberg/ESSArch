# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20170303_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagemethod',
            name='targets',
            field=models.ManyToManyField(related_name='methods', through='storage.StorageMethodTargetRelation', to='storage.StorageTarget'),
        ),
    ]
