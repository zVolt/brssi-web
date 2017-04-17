from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import *
from .models import Notice, Testimonial, Upload
from .models import Student, TestAttempt, BoardResultType, Faculty


def is_student(user):
    return user in Group.objects.get(name='students').user_set.all()


def is_faculty(user):
    return user in Group.objects.get(name='faculties').user_set.all()


def is_admin(user):
    return user in Group.objects.get(name='admin').user_set.all()


def redirectUser(request):
    data = dict()
    if request.user in Group.objects.get(name='students').user_set.all():
        return redirect('/student/')
    elif request.user in Group.objects.get(name='faculties').user_set.all():
        return redirect('/faculty/')
    elif request.user in Group.objects.get(name='admin').user_set.all():
        return redirect('/moderator/')
    else:
        data['result'] = False
        data['msg'] = 'Cannot recognize you'
        return render(request, 'home/login.html', data)


def index(request):
    data = dict()
    data['notices'] = Notice.objects.all()
    data['testimonials'] = Testimonial.objects.all()
    return render(request, 'home/index.html', data)


def disclaimer(request):
    return render(request, 'home/disclaimer.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/login/')


def user_login(request):
    data = dict()
    if request.user.is_authenticated():
        return redirectUser(request)
    if request.method == 'POST':
        username = request.POST['userid']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirectUser(request)
        else:
            data['result'] = False
            data['msg'] = 'Username and Password combination is incorrect! Try again.'
    return render(request, 'home/login.html', data)


@login_required
@user_passes_test(is_student)
def student(request):
    data = dict()
    return render(request, 'home/student.html', data)


@login_required
@user_passes_test(is_student)
def student_profile(request):
    data = dict()
    student = None
    try:
        student = Student.objects.get(user=request.user)
    except Exception as err:
        # I doubt that a user is likely to reach this point
        data['result'] = False
        data['msg'] = 'You are not a student'
        data['error'] = str(err)
    else:
        if request.method == 'GET':
            if student:
                data['student_form'] = FoundationStudentForm(instance=student)
        elif request.method == 'POST':
            try:
                student_form = StudentForm(request.POST, instance=student)
                student = student_form.save(commit=False)
                student.user = request.user
                student.save()
                data['result'] = True
                data['msg'] = 'Your details are updated!'
                data['student_form'] = StudentForm(instance=student)
            except Exception as err:
                data['result'] = False
                data['msg'] = 'Error saving new data'
                data['error'] = str(err)
        return render(request, 'home/student_profile.html', data)


@login_required
@user_passes_test(is_student)
def student_material(request):
    data = dict()
    return render(request, 'home/student_material.html', data)


def student_scholarship(request):
    data = dict()
    return render(request, 'home/student_scholarship.html', data)


@login_required
@user_passes_test(is_student)
def student_scholarship_apply(request):
    data = dict()
    try:
        data['scholarship_form'] = ScholarshipForm()
    except Exception as ex:
        data['result'] = False
        data['error'] = str(ex)
    return render(request, 'home/student_scholarship_apply.html', data)


@login_required
@user_passes_test(is_student)
def student_result(request):
    data = dict()
    data['attempts'] = TestAttempt.objects.filter(student__user=request.user)
    return render(request, 'home/student_result.html', data)


def faculty(request):
    data = dict()
    try:
        data['faculties'] = Faculty.objects.all()
        data['result'] = True
    except Exception as ex:
        data['result'] = False
        data['msg'] = str(ex)
    return render(request, 'home/faculty.html', data)


@login_required
@user_passes_test(is_admin)
def moderator(request):
    data = dict()
    return render(request, 'home/moderator.html', data)


def student_board_result(request):
    data = dict()
    try:
        result_map = dict()
        for board_type in BoardResultType.objects.all():
            result_map[board_type.name] = board_type.boardresult_set.all()
        data['result_map'] = result_map
        data['result'] = True
        print data
    except Exception as ex:
        data['result'] = False
        data['msg'] = str(ex)
    return render(request, 'home/board_result.html', data)


def admission(request, type=None):
    data = dict()
    if request.method == 'POST':
        if type == 'foundation':
            data['heading'] = 'Foundation Admission Form'
            form=FoundationStudentForm(request.POST)
            if form.is_valid():
                form.save()
                data['msg']='saved foundation'
            else:
                data['form'] = form
        elif type == 'engineering':
            data['heading'] = 'Engineering Admission Form'
            form=EngineeringStudentForm(request.POST)
            if form.is_valid():
                form.save();
                data['msg']='saved engineering'
            else:
                data['form'] = form
    else:
        if type == 'foundation':
            data['form'] = FoundationStudentForm()
            data['heading'] = 'Foundation Admission Form'
        elif type == 'engineering':
            data['form'] = EngineeringStudentForm()
            data['heading'] = 'Engineering Admission Form'
    if 'form' in data.keys():
        data['half'] = len(data['form'].fields) / 2
    data['offline_foundation_form']=Upload.objects.get(type=Upload.TYPE_ADMISSION_FORM)
    return render(request, 'home/admission.html', data)


def send_email(request):
    from django.conf import settings
    if settings.EMAIL and settings.EMAIL_PASSWORD:
        gm = Gmail(settings.EMAIL, settings.EMAIL_PASSWORD)
        gm.send_message('Subject', 'Message')
    return index(request)


import smtplib


class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.brssi.in'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + 'zkhan1093@gmail.com',
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.email,
            headers + "\r\n\r\n" + body)
