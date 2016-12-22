# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0023_auto_20161208_1047'),
    ]

    operations = [
        # Copy from 0023 migration but set db_index=False to remove index
        migrations.AlterField(
            model_name='eventip',
            name='eventApplication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='WorkflowEngine.ProcessTask', db_index=False),
        ),
        migrations.AlterField(
            model_name='eventip',
            name='eventApplication',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='WorkflowEngine.ProcessTask'),
        ),
    ]
