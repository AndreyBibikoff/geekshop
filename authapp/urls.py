# from django.conf.urls import url
from django.urls import path

import authapp.views as authapp
from django.urls import re_path

app_name="authapp"

urlpatterns = [
    re_path(r'^login/$', authapp.login, name='login'),
    re_path(r'^logout/$', authapp.logout, name='logout'),
    re_path(r'^register/$', authapp.register, name='register'),
    re_path(r'^edit/$', authapp.edit, name='edit'),
    path('verify/<email>/<key>', authapp.verify, name="verify")
    
]

    