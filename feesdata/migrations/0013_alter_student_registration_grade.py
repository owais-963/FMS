# Generated by Django 3.2.9 on 2021-11-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feesdata', '0012_auto_20211110_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_registration',
            name='grade',
            field=models.CharField(max_length=2, verbose_name='Class'),
        ),
    ]
