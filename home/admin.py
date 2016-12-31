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


@admin.register(Subject)
class AdminSubject(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Qualification)
class AdminQualification(admin.ModelAdmin):
    list_display = ('qualification_name', 'school', 'board', 'result')


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('name', 'mothers_name','date_of_birth','gender','joined_on')


@admin.register(Faculty)
class AdminFaculty(admin.ModelAdmin):
    list_display = ('name', 'email_address','highest_qualification')


@admin.register(Testimonial)
class AdminTestimonial(admin.ModelAdmin):
    list_display = ('content','name')
    filter_list=('name')