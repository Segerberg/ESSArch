# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def link_tag_version_types(apps, schema_editor):
    TagVersion = apps.get_model('tags', 'TagVersion')
    TagVersionType = apps.get_model('tags', 'TagVersionType')

    for tag_version in TagVersion.objects.all().iterator():
        tag_version_type, created = TagVersionType.objects.get_or_create(name=tag_version.type)
        tag_version.type_link = tag_version_type
        tag_version.save()


def link_structure_unit_types(apps, schema_editor):
    Structure = apps.get_model('tags', 'Structure')
    StructureType = apps.get_model('tags', 'StructureType')
    StructureUnit = apps.get_model('tags', 'StructureUnit')
    StructureUnitType = apps.get_model('tags', 'StructureUnitType')

    if Structure.objects.exists():
        structure_type, _ = StructureType.objects.get_or_create(name='temp')

        for unit in StructureUnit.objects.all().iterator():
            unit_type, created = StructureUnitType.objects.get_or_create(name=unit.type, defaults={'structure_type': structure_type})
            unit.type_link = unit_type
            unit.save()


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('tags', '0018_auto_20190325_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagVersionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='structureunit',
            name='type_link',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.StructureUnitType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tagversion',
            name='type_link',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.TagVersionType'),
            preserve_default=False,
        ),
        migrations.RunPython(link_tag_version_types, migrations.RunPython.noop),
        migrations.RunPython(link_structure_unit_types, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='structureunit',
            name='type',
        ),
        migrations.RemoveField(
            model_name='tagversion',
            name='type',
        ),
    ]
