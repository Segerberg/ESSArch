# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-15 07:58
from __future__ import unicode_literals

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0063_auto_20170331_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='processtask',
            name='args',
            field=picklefield.fields.PickledObjectField(default=[], editable=False, null=True),
        ),
    ]