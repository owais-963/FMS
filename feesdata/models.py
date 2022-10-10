from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Admin_registration(models.Model):
    user_Name = models.CharField('User Name', max_length=200, null=False)
    user_Email = models.EmailField('User Email', null=False)
    user_designation = models.CharField('User Designation', max_length=100, null=False)
    user_password = models.CharField('Password', max_length=200, null=False)
    date_of_registration = models.DateTimeField('User registration date'
                                                , default=datetime.datetime.now)


class Fees_and_grades_details(models.Model):
    grade = models.IntegerField('Grade', null=False, )
    fees = models.IntegerField('Fees', null=False)
    total = models.IntegerField('Total no of student in class', null=False)


class Student_registration(models.Model):
    name = models.CharField('First Name', null=False, max_length=200)
    father_name = models.CharField('Father Name', null=False, max_length=200)
    father_cnic_no = models.CharField('Father CNIC no', null=False, max_length=15)
    grade = models.IntegerField('Class', null=False)
    father_contact_no = models.CharField('Father Contact no', null=False, max_length=12)
    email = models.EmailField('Email Address', blank=True)
    home_phone_no = models.CharField('Home Phone No', null=True, blank=True, max_length=15)
    address = models.TextField('Address')
    gender = models.CharField("Gender", null=False, max_length=6)
    image = models.ImageField(default='images/profile_pic.png', upload_to='images/')
    # date_of_registration = models.DateTimeField('User registration date'
    #                                             , default=datetime.datetime.now)


class fees_collection(models.Model):
    fee_id = models.ForeignKey(Student_registration, on_delete=models.CASCADE)
    month = models.CharField("Month", max_length=20,
                             default=datetime.datetime.now().strftime("%B") + " "
                                     + datetime.datetime.now().strftime("%Y"))
    status = models.CharField("Status", max_length=100, null=False)
    payment_date = models.DateTimeField('Payment Date'
                                        , default=datetime.datetime.now)
    collected_by = models.CharField("Collector Name", max_length=200, null=False)
