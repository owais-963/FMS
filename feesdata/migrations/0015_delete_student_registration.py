# Generated by Django 3.2.9 on 2021-11-10 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feesdata', '0014_remove_student_registration_grade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student_registration',
        ),
    ]
