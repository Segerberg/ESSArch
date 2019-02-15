"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch Core
    Copyright (C) 2005-2017 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('progress', models.IntegerField(blank=True, default=0)),
                ('type', models.IntegerField(choices=[(-1, 'Undefined'), (0, 'Success'), (1, 'Error'), (2, 'Warning')], null=True)),
                ('user', models.CharField(max_length=45)),
                ('result', picklefield.fields.PickledObjectField(blank=True, editable=False)),
                ('status', models.IntegerField(blank=True, choices=[(-1, 'Undefined'), (0, 'Success'), (1, 'Error'), (2, 'Warning')], default=0)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('hidden', models.BooleanField(default=False)),
                ('information_package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='ip.InformationPackage')),
            ],
            options={
                'db_table': 'ProcessStep',
            },
        ),
        migrations.CreateModel(
            name='ProcessTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('progress', models.IntegerField(blank=True, default=0)),
                ('task_id', models.CharField(max_length=255, unique=True, verbose_name='task id')),
                ('status', models.CharField(choices=[('FAILURE', 'FAILURE'), ('PENDING', 'PENDING'), ('RECEIVED', 'RECEIVED'), ('RETRY', 'RETRY'), ('REVOKED', 'REVOKED'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=50, verbose_name='state')),
                ('result', picklefield.fields.PickledObjectField(default=None, editable=False, null=True)),
                ('date_done', models.DateTimeField(auto_now=True, verbose_name='done at')),
                ('traceback', models.TextField(blank=True, null=True, verbose_name='traceback')),
                ('hidden', models.BooleanField(db_index=True, default=False, editable=False)),
                ('meta', picklefield.fields.PickledObjectField(default=None, editable=False, null=True)),
                ('processstep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WorkflowEngine.ProcessStep')),
            ],
            options={
                'db_table': 'ProcessTask',
            },
        ),
    ]
