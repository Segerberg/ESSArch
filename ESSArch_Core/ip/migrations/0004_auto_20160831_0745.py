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
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20160830_1023'),
        ('ip', '0003_auto_20160823_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informationpackage',
            name='SubmissionAgreement',
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='SA',
            field=models.ForeignKey(on_delete=models.CASCADE, default=None, to='profiles.SubmissionAgreement', null=True),
        ),
    ]
