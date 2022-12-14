# Generated by Django 3.2.9 on 2021-11-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feesdata', '0015_delete_student_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('mid_name', models.CharField(blank=True, max_length=100, verbose_name='Mid Name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Last Name')),
                ('father_name', models.CharField(max_length=200, verbose_name='Father Name')),
                ('father_cnic_no', models.CharField(max_length=15, verbose_name='Father CNIC no')),
                ('father_contact_no', models.CharField(max_length=12, verbose_name='Father Contact no')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('home_phone_no', models.CharField(blank=True, max_length=15, null=True, verbose_name='Home Phone No')),
                ('address', models.TextField(verbose_name='Address')),
                ('image', models.ImageField(default='media/images/profile_pic.png', upload_to='')),
            ],
        ),
    ]
