# Generated by Django 5.0.4 on 2024-04-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0016_subjectdetails_student_user_dept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectdetails',
            name='student',
        ),
        migrations.AlterField(
            model_name='user',
            name='joining_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
