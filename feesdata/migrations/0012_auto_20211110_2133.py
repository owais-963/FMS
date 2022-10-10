# Generated by Django 3.2.9 on 2021-11-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feesdata', '0011_student_registration_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees_and_grades_details',
            name='collect_amount',
        ),
        migrations.RemoveField(
            model_name='fees_and_grades_details',
            name='no_of_student',
        ),
        migrations.AddField(
            model_name='student_registration',
            name='grade',
            field=models.IntegerField(default=1, verbose_name='Class'),
            preserve_default=False,
        ),
    ]