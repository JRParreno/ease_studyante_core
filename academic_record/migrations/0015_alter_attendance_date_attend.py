# Generated by Django 3.2 on 2024-03-19 23:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('academic_record', '0014_alter_attendance_date_attend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_attend',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
