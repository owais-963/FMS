# Generated by Django 3.2.9 on 2021-11-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feesdata', '0016_student_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_registration',
            name='grade',
            field=models.IntegerField(default=0, verbose_name='Class'),
            preserve_default=False,
        ),
    ]