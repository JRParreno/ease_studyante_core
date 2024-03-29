# Generated by Django 3.2 on 2024-03-13 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class_information', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N/A', 'N/A')], default='N/A', max_length=10)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/profiles/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teacher_department', to='class_information.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N/A', 'N/A')], default='N/A', max_length=10)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/profiles/')),
                ('year_level', models.CharField(choices=[('GRADE 7', 'Grade 7'), ('GRADE 8', 'Grade 8'), ('GRADE 9', 'Grade 9'), ('GRADE 10', 'Grade 10'), ('GRADE 11', 'Grade 11'), ('GRADE 12', 'Grade 12')], default='GRADE 7', max_length=10)),
                ('qr_code_photo', models.ImageField(upload_to='images/qr_code/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N/A', 'N/A')], default='N/A', max_length=10)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/profiles/')),
                ('students', models.ManyToManyField(related_name='kids', to='user_profile.Student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
