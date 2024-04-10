# Generated by Django 5.0.4 on 2024-04-09 06:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_department_profiledetails_delete_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
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
    ]
