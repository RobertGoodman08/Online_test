from django.urls import path
from user.views import user_login,user_logout, logout, register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
