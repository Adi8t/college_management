# Generated by Django 5.0.4 on 2024-04-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0018_user_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joining_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
