# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0048_auto_20190529_1043'),
        ('ip', '0078_auto_20190406_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventip',
            name='delivery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='tags.Delivery', verbose_name='delivery'),
        ),
        migrations.AddField(
            model_name='eventip',
            name='transfer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='tags.Transfer', verbose_name='transfer'),
        ),
    ]
