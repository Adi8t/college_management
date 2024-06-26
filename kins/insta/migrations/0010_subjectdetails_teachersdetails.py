# Generated by Django 5.0.4 on 2024-04-09 07:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0009_alter_department_user_alter_user_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectDetails',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('subject_code', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='subjects_taught', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'subject_details',
            },
        ),
        migrations.CreateModel(
            name='TeachersDetails',
            fields=[
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_email', models.CharField(max_length=100, unique=True)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('Department', models.CharField(max_length=100, null=True)),
                ('subject_taught', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.subjectdetails')),
            ],
        ),
    ]
