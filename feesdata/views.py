import datetime

from django.shortcuts import render, redirect
from . import models
from django.contrib import messages as msg
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def dwonload_form(request):
    data = {}
    if request.is_ajax():
        data['name'] = request.POST.get('name')
        data['file'] = request.FILES.get('img')
        return HttpResponse(data['file'])
    else:
        return render(request,'feesdata/pages/test.html')

    # if request.session.has_key('user_loged'):
    #     if request.POST:
    #         pdf = request.FILES('data')
    #         return HttpResponse(pdf, content_type='application/pdf')
    #     pdf=request.FILES['form']
    #     return HttpResponse(pdf, content_type='application/pdf')


@csrf_exempt
def add(request):
    a = request.POST.get("data")
    # b = request.POST.get("b")

    # a = float(a)
    # b = float(b)
    # c = a + b
    return HttpResponse(a)


def login(request):
    if request.session.has_key('user_loged'):
        return redirect('dashboard')
    elif request.POST:
        user_name = 'user_Name' in request.POST
        user_email = request.POST['user_Email']
        user_password = request.POST['user_password']
        user_designation = request.POST['user_designation']
        user_designation = user_designation.lower()

        validation1 = models.Admin_registration.objects.filter(user_Email=user_email).count()
        validation2 = models.Admin_registration.objects.filter(user_designation=user_designation).count()

        if (validation1 == 0) & (validation2 == 0):
            register = models.Admin_registration(user_Name=user_name, user_Email=user_email,
                                                 user_password=user_password,
                                                 user_designation=user_designation)
            register.save()

            return redirect('login')
        else:
            msg.error(request, 'Email or Designation is already used')
            return redirect('signup')

    return render(request, 'feesdata/pages/signin.html')


def signup(request):
    return render(request, 'feesdata/pages/signup.html')


def dashboard(request):
    if request.session.has_key('user_loged'):
        return render(request, 'feesdata/pages/dashboard.html', un_paid())
    elif request.POST:
        user_email = request.POST['user_Email']
        user_password = request.POST['user_password']
        checking_for_user = models.Admin_registration.objects.filter(user_Email=user_email,
                                                                     user_password=user_password).count()

        if checking_for_user > 0:
            request.session['user_loged'] = True
            request.session['user_id'] = models.Admin_registration.objects.values('id').filter(user_Email=user_email,
                                                                                               user_password=user_password)[
                0]['id']
            global login_id
            login_id = models.Admin_registration.objects.values('id').filter(user_Email=user_email,
                                                                             user_password=user_password)

            return render(request, 'feesdata/pages/dashboard.html', un_paid())
        else:
            msg.error(request, "user not found")
            return redirect('login')
    else:
        return redirect('login')


def logout(request):
    if request.session.has_key:
        del request.session['user_loged']
        return redirect('login')


def feedata(request):
    if request.session.has_key('user_loged'):
        if request.POST:
            grade = request.POST['class']
            fees = request.POST['fees']
            data = models.Student_registration.objects.all().filter(grade=grade).count()
            obj = models.Fees_and_grades_details.objects.all().filter(
                grade=grade
            )
            check = obj.count()
            if check > 0:
                obj.update(fees=fees, total=data)
            else:
                create_obj = models.Fees_and_grades_details(grade=grade, fees=fees,
                                                            total=data)
                create_obj.save()
            return redirect('fees_data')
            # update.fees = fees
            # update.total = data
            # data = models.Fees_and_grades_details.objects.all()
            # return render(request, 'feesdata/pages/feesdata.html',{'data': data})
        else:

            obj = models.Fees_and_grades_details()

            tf_collected = 0

            data = models.Fees_and_grades_details.objects.order_by('grade').all()

            for d in data:
                tf_collected += d.fees * d.total

            total_s = models.Fees_and_grades_details.objects.values('total')
            total_fee = models.Fees_and_grades_details.objects.values('fees')

            ts = 0
            for t_s in total_s:
                ts += t_s['total']

            tf = 0
            for t_f in total_fee:
                tf += t_f['fees']

            # total_s = total_s
            # total_s = str(total_s)
            # # total_fee = list(total_fee)
            # # total_s = sum(total_s)
            # # total_fee = sum(total_fee)

            return render(request, 'feesdata/pages/feesdata.html',
                          {'data': data, 'len': total_s, 'fee': total_fee, 'ts': ts, 'tf': tf, 'tf_c': tf_collected})

        # alist = models.Fees_and_grades_details.objects.all().count()
        # count = []
        # for i in range(1, alist + 1):
        #     data = models.Student_registration.all().filter(grade=i)
        #     x = data.count()
        #     count.append(x)


def student_registration(request):
    if request.session.has_key:
        if request.POST:
            name = request.POST['name']
            father_name = request.POST['father_name']
            grade = request.POST['class']
            cnic_no = request.POST['cnic']
            father_contact_number = request.POST['father_contact_number']
            email = request.POST['email']
            home_phone_no = request.POST['home_contact_number']
            address = request.POST['address']
            img = request.FILES['img']
            gender = request.POST['gender']

            student = models.Student_registration(
                name=name,
                father_name=father_name,
                father_cnic_no=cnic_no,
                grade=grade,
                father_contact_no=father_contact_number,
                email=email,
                home_phone_no=home_phone_no,
                address=address,
                image=img,
                gender=gender
            )

            validation = models.Student_registration.objects.filter(name=name,
                                                                    father_cnic_no=cnic_no).count()

            if validation == 0:
                student.save()
                no_of_student = models.Student_registration.objects.all().filter(grade=grade).count()
                update = models.Fees_and_grades_details.objects.all().filter(grade=grade)
                update.update(total=no_of_student)
                data = models.Student_registration.objects.all().filter(
                    name=name,
                    father_cnic_no=cnic_no, father_name=father_name
                )
                return render(request, 'feesdata/pages/genrated_form.html', {'data': data})

            else:
                return HttpResponse("FUCKING ERROR")

        return render(request, 'feesdata/pages/student_registration_form.html')


def class_detail(request, grade):
    if request.session.has_key:
        data = models.Student_registration.objects.order_by('id').all().filter(grade=grade)
        return render(request, 'feesdata/pages/class_detail.html', {"data": data})


def student_data(request, id):
    if request.session.has_key:
        if request.POST:
            name = request.POST['name']
            father_name = request.POST['father_name']
            grade = request.POST['class']
            cnic_no = request.POST['cnic']
            father_contact_number = request.POST['father_contact_number']
            email = request.POST['email']
            home_phone_no = request.POST['home_contact_number']
            address = request.POST['address']

            img = request.FILES.get('img', False)

            gender = request.POST['gender']

            obj = models.Student_registration.objects.filter(id=id)

            obj.update(
                name=name,
                father_name=father_name,
                father_cnic_no=cnic_no,
                grade=grade,
                father_contact_no=father_contact_number,
                email=email,
                home_phone_no=home_phone_no,
                address=address,
                gender=gender,
            )

            obj = models.Student_registration.objects.get(id=id)

            if img != False:
                obj.image = img
                obj.save()

            return redirect("student_data", id=id)
        else:
            data = models.Student_registration.objects.all().filter(id=id)
            fees_data = models.fees_collection.objects.all().filter(fee_id=id)
            return render(request, 'feesdata/pages/student_detail.html', {'data': data, 'fee_data': fees_data})


def edit_student_data(request, id):
    if request.session.has_key:
        data = models.Student_registration.objects.order_by('id').all().filter(id=id)
        return render(request, 'feesdata/pages/student_data_edit.html', {'data': data})


def fees_pay(request):
    if request.session.has_key:
        if request.POST:
            name = request.POST['name']
            grade = request.POST['class_filter']
            data = not models.Student_registration.objects.order_by('id').all(). \
                filter(name=name, grade=grade)
            if len(data) == 0:
                data = 0
            return render(request, 'feesdata/pages/fees_voucher.html', {'data': data, 'range': list(range(1, 11))})
        else:
            student = models.Student_registration.objects.all()

            obj_list = []
            c = []

            for i in range(1, len(student) + 1):
                count = models.fees_collection.objects.all().filter(fee_id=i,
                                                                    month=datetime.datetime.now().strftime("%B")
                                                                          + " " + datetime.datetime.now().strftime(
                                                                        "%Y")).count()
                c.append(count)
                if count == 0:
                    obj = student.filter(id=i)
                    obj_list.append(obj)
            data = obj_list
            return render(request, 'feesdata/pages/fees_voucher.html',{'data' : data, 'range': list(range(1, 11))})


def voucher(request, id, grade):
    if request.session.has_key:
        data = models.Student_registration.objects.all().filter(id=id)
        fee = models.Fees_and_grades_details.objects.all().filter(grade=grade)
        if request.POST:
            collector = models.Admin_registration.objects.values('user_Name').filter(id=request.session['user_id'])
            fee_pay = models.fees_collection(status="Paid", collected_by=collector)
            fee_pay.fee_id_id = id
            check = models.fees_collection.objects.all().filter(fee_id=id,
                                                                month=datetime.datetime.now().strftime("%B")
                                                                      + " " + datetime.datetime.now().strftime(
                                                                    "%Y")).count()
            if check < 1:
                fee_pay.save()
                collected = models.fees_collection.objects.all().filter(fee_id=id,
                                                                        month=datetime.datetime.now().strftime("%B")
                                                                              + " " + datetime.datetime.now().strftime(
                                                                            "%Y"))
                return render(request,'feesdata/pages/fee_voucher_generated.html',
                                     {'data': data, 'fee': fee, 'fees': collected})
                # return pdf_generator1('feesdata/pages/fee_voucher_generated.html',
                #                       {'data': data, 'fee': fee, 'fees': collected})
                # # return render(request, 'feesdata/pages/fee_voucher_generated.html',
                #               {'data': data, 'fee': fee, 'status': 1})
            else:
                return HttpResponse("Fucking Error")
        else:
            return render(request, 'feesdata/pages/fee_voucher_generated.html', {'data': data, 'fee': fee})


def un_paid():
    student = models.Student_registration.objects.all()

    obj_list = []
    c = []

    for i in range(1, len(student) + 1):
        count = models.fees_collection.objects.all().filter(fee_id=i, month=datetime.datetime.now().strftime("%B")
                                                                            + " " + datetime.datetime.now().strftime(
            "%Y")).count()
        c.append(count)
        if count == 0:
            obj = student.filter(id=i)
            obj_list.append(obj)

    data = {'data': obj_list}

    return data


def pdf_generator(context, parm: dict):
    from io import BytesIO
    from django.template.loader import get_template
    import xhtml2pdf.pisa as pisa

    template = get_template(context)
    html = template.render(parm)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
#
#
# def pdf_generator1(context, parm: dict):
#     from django.template.loader import get_template
#     from random import randint
#     from uuid import uuid4
#     import pdfkit
#     import os
#
#     filename = 'student/id.pdf'
#
#     # HTML FIle to be converted to PDF - inside your Django directory
#     template = get_template(context)
#
#     # Render the HTML
#     html = template.render(parm)
#
#     # Options - Very Important [Don't forget this]
#     options = {
#         'encoding': 'UTF-8',
#         'javascript-delay': '10',  # Optional
#         'enable-local-file-access': None,  # To be able to access CSS
#         'page-size': 'A5',
#         'custom-header': [
#             ('Accept-Encoding', 'gzip')
#         ],
#     }
#     # Javascript delay is optional
#
#     # Remember that location to wkhtmltopdf
#     config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf')
#
#     css1 = os.path.join(settings.CSS_LOCATION, 'static', 'style.css')
#
#
#     file_content = pdfkit.from_string(html, False, configuration=config, options=options)
#
#     # Create the HTTP Response
#     response = HttpResponse(file_content, content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename = {}'.format(filename)
#
#     # Return
#     return response
#
# def weasy_pdf(context,data):
#     from weasyprint import CSS, HTML
#     from django.template.loader import render_to_string
#     from django.core.files.storage import FileSystemStorage
#
#     filename = 'student/id'
#
#     html_string = render_to_string(context,data)
#
#     html = HTML(string=html_string).write_pdf(
#         target=filename,
#         stylesheets=[
#             CSS("\static\style.css"),
#             CSS("https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"),
#             CSS("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css")
#         ],
#     )
#
#     # Instantiate FileStorage.
#     fs = FileSystemStorage("")
#
#     with fs.open(filename) as pdf:
#         response = HttpResponse(pdf, content_type="application/pdf")
#         response["Content-Disposition"] = 'attachment; filename="%s.pdf"'%(filename)
#         return response
