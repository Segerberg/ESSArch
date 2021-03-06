"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch
    Copyright (C) 2005-2019 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20160830_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileRel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'Disabled'), (1, 'Enabled'), (2, 'Default')], default=0, verbose_name='Profile status')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
            options={
                'ordering': ['status'],
                'verbose_name': 'ProfileRel',
            },
        ),
        migrations.AddField(
            model_name='profilerel',
            name='submissionagreement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.SubmissionAgreement'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profiles',
            field=models.ManyToManyField(related_name='submission_agreements', through='profiles.ProfileRel', to='profiles.Profile'),
        ),
    ]
