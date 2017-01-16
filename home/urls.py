from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),

    url(r'^student/$', views.student, name='login'),
    url(r'^student/profile/$', views.student_profile, name='login'),
    url(r'^student/study-material/$', views.student_material, name='login'),
    url(r'^student/scholarship/$', views.student_scholarship, name='login'),
    url(r'^student/result/$', views.student_result, name='login'),

    url(r'^faculty/$', views.faculty, name='login'),
    url(r'^moderator/$', views.moderator, name='login'),
    url(r'^disclaimer/$', views.disclaimer, name='disclaimer'),
]
