from django.contrib import admin

from .models import *


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_on')


@admin.register(Branch)
class AdminBranch(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Board)
class AdminBoard(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FoundationSubject)
class AdminFoundationSubject(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(EngineeringSubject)
class AdminEngineeringSubject(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Programme)
class AdminProgramme(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Qualification)
class AdminQualification(admin.ModelAdmin):
    list_display = ('qualification_name', 'school', 'board', 'result')

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('user', 'mother_name', 'date_of_birth', 'gender', 'joined_on')

@admin.register(FoundationStudent)
class AdminFoundationStudent(admin.ModelAdmin):
    list_display = ('user', 'mother_name', 'date_of_birth', 'gender', 'joined_on')


@admin.register(EngineeringStudent)
class AdminEngineeringStudent(admin.ModelAdmin):
    list_display = ('user', 'mother_name', 'date_of_birth', 'gender', 'joined_on')


@admin.register(Faculty)
class AdminFaculty(admin.ModelAdmin):
    list_display = ('user', 'highest_qualification')


@admin.register(Testimonial)
class AdminTestimonial(admin.ModelAdmin):
    list_display = ('content', 'name')
    filter_list = ('name')


@admin.register(Test)
class AdminTest(admin.ModelAdmin):
    list_display = ('test_code', 'subject', 'total_marks')
    filter_list = ('subject')


@admin.register(TestAttempt)
class AdminTestAttempt(admin.ModelAdmin):
    list_display = ('student', 'test', 'date_of_examination', 'marks_obtained', 'remarks')
    filter_list = ('date_of_examination', 'faculty', 'student', 'test')


@admin.register(Scholarship)
class AdminScholarship(admin.ModelAdmin):
    list_display = (
        'student', 'marks_in_board_exam', 'marks_in_institute_exam', 'monthly_family_income', 'other_scholarship',
        'applied_on')
    filter_list = (
        'monthly_family_income', 'other_scholarship', 'marks_in_board_exam', 'marks_in_institute_exam', 'applied_on')


@admin.register(BoardResultType)
class AdminBoardResultType(admin.ModelAdmin):
    list_display = ('name', 'author', 'added_on')
    filter_list = ('added_on', 'author')


@admin.register(BoardResult)
class AdminBoardResult(admin.ModelAdmin):
    list_display = ('name', 'link', 'author', 'added_on')
    filter_list = ('added_on', 'author')


@admin.register(Upload)
class AdminBoardResult(admin.ModelAdmin):
    list_display = ('file', 'type')
    filter_list = ('type')