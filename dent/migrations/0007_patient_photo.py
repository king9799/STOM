# Generated by Django 3.2.11 on 2022-03-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dent', '0006_remove_patient_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]