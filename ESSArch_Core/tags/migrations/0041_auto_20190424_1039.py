# Generated by Django 2.0.13 on 2019-04-24 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0040_auto_20190424_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='structuretype',
            old_name='editable_instance_units',
            new_name='editable_instances',
        ),
    ]
