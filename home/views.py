from django.shortcuts import render,redirect
from .models import Notice, Testimonial
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import StudentForm
from .models import Student,TestAttempt

def is_student(user):
    return user in Group.objects.get(name='students').user_set.all()


def is_faculty(user):
    return user in Group.objects.get(name='faculties').user_set.all()


def is_admin(user):
    return user in Group.objects.get(name='admin').user_set.all()


def redirectUser(request):
    data=dict()
    if request.user in Group.objects.get(name='students').user_set.all():
        return redirect('/student/')
    elif request.user in Group.objects.get(name='faculties').user_set.all():
        return redirect('/faculty/')
    elif request.user in Group.objects.get(name='admin').user_set.all():
        return redirect('/moderator/')
    else:
        data['result']=False
        data['msg']='Cannot recognize you'
        return render(request,'home/login.html',data)


def index(request):
    data=dict()
    data['notices']=Notice.objects.all()
    data['testimonials']=Testimonial.objects.all()
    return render(request,'home/index.html',data)


def disclaimer(request):
    return render(request,'home/disclaimer.html')


def user_login(request):
    data=dict()
    if request.user.is_authenticated():
        return redirectUser(request)
    if request.method=='POST':
        username=request.POST['userid']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            redirectUser(request)
        else:
            data['result']=False
            data['msg']='Username and Password combination is incorrect! Try again.'
    return render(request,'home/login.html',data)


@login_required
@user_passes_test(is_student)
def student(request):
    data=dict()
    return render(request,'home/student.html',data)


@login_required
@user_passes_test(is_student)
def student_profile(request):
    data=dict()
    student=None
    try:
        student=Student.objects.get(user=request.user)
    except Exception as err:
        # I doubt that a user is likely to reach this point
        data['result']=False
        data['msg']='You are not a student'
        data['error']=str(err)
    else:
        if request.method=='GET':
            if student:
                data['student_form']=StudentForm(instance=student)
        elif request.method=='POST':
            try:
                student_form=StudentForm(request.POST,instance=student)
                student=student_form.save(commit=False)
                student.user=request.user
                student.save()
                data['result']=True
                data['msg']='Your details are updated!'
                data['student_form']=StudentForm(instance=student)
            except Exception as err:
                data['result']=False
                data['msg']='Error saving new data'
                data['error']=str(err)
        return render(request,'home/student_profile.html',data)


@login_required
@user_passes_test(is_student)
def student_material(request):
    data=dict()
    return render(request,'home/student_material.html',data)


@login_required
@user_passes_test(is_student)
def student_scholarship(request):
    data=dict()
    return render(request,'home/student_scholarship.html',data)


@login_required
@user_passes_test(is_student)
def student_result(request):
    data=dict()
    data['attempts']=TestAttempt.objects.filter(student__user=request.user)
    return render(request,'home/student_result.html',data)


@login_required
@user_passes_test(is_faculty)
def faculty(request):
    data=dict()
    return render(request,'home/faculty.html',data)


@login_required
@user_passes_test(is_admin)
def moderator(request):
    data=dict()
    return render(request,'home/moderator.html',data)
