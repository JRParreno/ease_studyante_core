# Generated by Django 3.2 on 2024-03-06 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20240305_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='delete_remarks',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='deleted_by_id',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='update_remarks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='delete_remarks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='student',
            name='deleted_by_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='update_remarks',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='delete_remarks',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='deleted_by_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='update_remarks',
        ),
    ]