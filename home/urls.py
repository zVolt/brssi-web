from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^student/$', views.student, name='login'),
    url(r'^faculty/$', views.faculty, name='login'),
    url(r'^moderator/$', views.moderator, name='login'),
    url(r'^disclaimer/$', views.disclaimer, name='disclaimer'),
]
