from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('feesdata', views.feedata, name='fees_data'),
    path('student_registration', views.student_registration, name='student_registration'),
    path('class/<int:grade>', views.class_detail, name='class_detail'),
    path('class/student_data/<int:id>', views.student_data, name='student_data'),
    path('student_data/edit/<int:id>', views.edit_student_data, name='edit_student_data'),
    path('fess_pay', views.fees_pay, name='fees_pay'),
    path('fees_pay/voucher/<int:id>/<int:grade>', views.voucher, name='voucher'),
    path('unpaid', views.un_paid, name='unpaid'),
    path('form', views.dwonload_form, name='form'),
    path('add', views.add, name='add')

]
