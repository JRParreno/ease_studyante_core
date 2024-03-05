# Generated by Django 3.2.22 on 2024-03-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('year_level', models.CharField(choices=[('GRADE 7', 'GRADE 7'), ('GRADE 8', 'GRADE 8'), ('GRADE 9', 'GRADE 9'), ('GRADE 10', 'GRADE 10'), ('GRADE 11', 'GRADE 11'), ('GRADE 12', 'GRADE 12')], default='GRADE 7', max_length=10)),
            ],
        ),
    ]
