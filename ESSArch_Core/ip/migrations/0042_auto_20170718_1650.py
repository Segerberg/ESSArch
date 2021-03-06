# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 14:50
from __future__ import unicode_literals

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    EventIP = apps.get_model("ip", "EventIP")
    db_alias = schema_editor.connection.alias
    EventIP.objects.using(db_alias).filter(eventOutcome=0).update(eventOutcome=20)
    EventIP.objects.using(db_alias).filter(eventOutcome=1).update(eventOutcome=40)


def reverse_func(apps, schema_editor):
    EventIP = apps.get_model("ip", "EventIP")
    db_alias = schema_editor.connection.alias
    EventIP.objects.using(db_alias).filter(eventOutcome__in=[10, 20, 30]).update(eventOutcome=0)
    EventIP.objects.using(db_alias).filter(eventOutcome__in=[40, 50]).update(eventOutcome=1)


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0041_auto_20170718_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventip',
            name='eventOutcome',
            field=models.IntegerField(choices=[(10, 'debug'), (20, 'info'), (30, 'warning'), (40, 'error'), (50, 'critical')], default=None, null=True),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]
