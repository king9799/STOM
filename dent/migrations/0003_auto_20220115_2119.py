# Generated by Django 3.2.11 on 2022-01-15 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dent', '0002_auto_20220114_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start',
            new_name='start_time',
        ),
    ]