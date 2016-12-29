from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Notice)
admin.site.register(Branch)
admin.site.register(Board)
admin.site.register(Student)
admin.site.register(Qualification)
admin.site.register(Subject)
admin.site.register(Faculty)