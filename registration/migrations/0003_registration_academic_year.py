# Generated by Django 3.2 on 2024-03-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_remove_registration_year_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='academic_year',
            field=models.CharField(default=2024, max_length=9),
            preserve_default=False,
        ),
    ]
