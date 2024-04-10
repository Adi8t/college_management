# Generated by Django 5.0.4 on 2024-04-09 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0010_subjectdetails_teachersdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachersdetails',
            name='teacher_email',
        ),
        migrations.AlterField(
            model_name='teachersdetails',
            name='subject_taught',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.subjectdetails'),
        ),
    ]
