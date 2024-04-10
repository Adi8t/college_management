# Generated by Django 5.0.4 on 2024-04-09 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('principal', 'Principal'), ('teacher', 'Teacher'), ('student', 'Student')], default='student', max_length=100),
        ),
        migrations.DeleteModel(
            name='SubjectDetails',
        ),
    ]
