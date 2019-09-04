# Generated by Django 2.0.13 on 2019-04-15 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0034_auto_20190411_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='structuretype',
            name='movable_instance_units',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='structure',
            name='template',
            field=models.ForeignKey(limit_choices_to={'is_template': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instances', to='tags.Structure', verbose_name='template'),
        ),
        migrations.AlterField(
            model_name='structureunit',
            name='template',
            field=models.ForeignKey(limit_choices_to={'structure__is_template': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instances', to='tags.StructureUnit', verbose_name='template'),
        ),
    ]