# Generated by Django 3.2 on 2024-03-13 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_information', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='department',
        ),
    ]