# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0073_processstep_context'),
        ('tags', '0015_auto_20181217_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediumType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('size', models.CharField(max_length=255, verbose_name='size')),
                ('unit', models.CharField(max_length=255, verbose_name='unit')),
            ],
        ),
        migrations.CreateModel(
            name='NodeIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.TextField(verbose_name='identifier')),
            ],
        ),
        migrations.CreateModel(
            name='NodeIdentifierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='NodeNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='text')),
                ('href', models.TextField(blank=True, verbose_name='href')),
                ('create_date', models.DateTimeField(verbose_name='create date')),
                ('revise_date', models.DateTimeField(null=True, verbose_name='revise date')),
            ],
        ),
        migrations.CreateModel(
            name='NodeNoteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='NodeRelationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='RuleConventionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='StructureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='StructureUnitRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('start_date', models.DateField(null=True, verbose_name='start date')),
                ('end_date', models.DateField(null=True, verbose_name='end date')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('revise_date', models.DateTimeField(auto_now=True, verbose_name='revise date')),
            ],
        ),
        migrations.CreateModel(
            name='StructureUnitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('structure_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.StructureType')),
            ],
        ),
        migrations.CreateModel(
            name='TagVersionRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('start_date', models.DateField(null=True, verbose_name='start date')),
                ('end_date', models.DateField(null=True, verbose_name='end date')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('revise_date', models.DateTimeField(auto_now=True, verbose_name='revise date')),
            ],
        ),
        migrations.AddField(
            model_name='structure',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='structures', to='WorkflowEngine.ProcessTask'),
        ),
        migrations.AddField(
            model_name='structureunit',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='structure_units', to='WorkflowEngine.ProcessTask'),
        ),
        migrations.AddField(
            model_name='tagstructure',
            name='end_date',
            field=models.DateField(null=True, verbose_name='end date'),
        ),
        migrations.AddField(
            model_name='tagstructure',
            name='start_date',
            field=models.DateField(null=True, verbose_name='start date'),
        ),
        migrations.AddField(
            model_name='tagversion',
            name='revise_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tagversionrelation',
            name='tag_version_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_version_relations_a', to='tags.TagVersion'),
        ),
        migrations.AddField(
            model_name='tagversionrelation',
            name='tag_version_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_version_relations_b', to='tags.TagVersion'),
        ),
        migrations.AddField(
            model_name='tagversionrelation',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tags.NodeRelationType'),
        ),
        migrations.AddField(
            model_name='structureunitrelation',
            name='structure_unit_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='structure_unit_relations_a', to='tags.StructureUnit'),
        ),
        migrations.AddField(
            model_name='structureunitrelation',
            name='structure_unit_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='structure_unit_relations_b', to='tags.StructureUnit'),
        ),
        migrations.AddField(
            model_name='structureunitrelation',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tags.NodeRelationType'),
        ),
        migrations.AddField(
            model_name='nodenote',
            name='structure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='tags.StructureUnit', verbose_name='structure unit'),
        ),
        migrations.AddField(
            model_name='nodenote',
            name='tag_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='tags.TagVersion', verbose_name='tag version'),
        ),
        migrations.AddField(
            model_name='nodenote',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tags.NodeNoteType', verbose_name='type'),
        ),
        migrations.AddField(
            model_name='nodeidentifier',
            name='structure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='tags.StructureUnit', verbose_name='structure unit'),
        ),
        migrations.AddField(
            model_name='nodeidentifier',
            name='tag_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='tags.TagVersion', verbose_name='tag version'),
        ),
        migrations.AddField(
            model_name='nodeidentifier',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tags.NodeIdentifierType', verbose_name='type'),
        ),
        migrations.AlterUniqueTogether(
            name='mediumtype',
            unique_together=set([('name', 'size', 'unit')]),
        ),
        migrations.AddField(
            model_name='structure',
            name='rule_convention_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tags.RuleConventionType'),
        ),
        migrations.AddField(
            model_name='structureunit',
            name='related_structure_units',
            field=models.ManyToManyField(through='tags.StructureUnitRelation', to='tags.StructureUnit'),
        ),
        migrations.AddField(
            model_name='tagversion',
            name='medium_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tag_versions', to='tags.MediumType'),
        ),
        migrations.AlterUniqueTogether(
            name='tagversionrelation',
            unique_together=set([('tag_version_a', 'tag_version_b', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='structureunitrelation',
            unique_together=set([('structure_unit_a', 'structure_unit_b', 'type')]),
        ),
    ]
