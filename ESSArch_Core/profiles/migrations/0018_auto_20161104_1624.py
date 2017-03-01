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
# Generated by Django 1.10 on 2016-11-04 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20161102_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_aip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_classification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_content_type',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_data_selection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_dip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_event',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_import',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_preservation_metadata',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_sip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_submit_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_transfer_project',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_workflow',
            field=models.BooleanField(default=False),
        ),
    ]