from django.contrib import admin
from quiz.views import home, result, questions
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', home, name='home'),
    path('result', result, name='result'),
    url(r'^(?P<choice>[\w]+)', questions, name='questions'),
]
