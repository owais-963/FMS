# Generated by Django 3.2.9 on 2021-11-09 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feesdata', '0004_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_registration',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='User registration date'),
        ),
    ]
