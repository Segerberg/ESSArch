# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-25 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentrelationtype',
            name='mirrored_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agents.AgentRelationType', verbose_name='mirrored type'),
        ),
    ]
