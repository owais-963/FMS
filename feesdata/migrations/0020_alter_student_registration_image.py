# Generated by Django 3.2.9 on 2021-11-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feesdata', '0019_auto_20211110_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_registration',
            name='image',
            field=models.ImageField(default='images/profile_pic.png', upload_to='images/'),
        ),
    ]
