from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('',views.base),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('usersignup/',views.usersignup,name='usersignup'),
    path('userlogout/',views.userlogut),
    path('otpverifcation/',views.otpverifcation,name='otpverify'),
    path('dashboard/',views.dashboard),
    path('events/',views.events),
    path('myprofile/',views.myprofile),
    path('notice/',views.notice),
    path('society_members/',views.society_members,name='society_members'),
    path('society_watchmen/',views.society_watchmen,name='society_watchmen'),
    path('forgotpass/',views.forgotpass),
    path('fotpverify/',views.fotpverify,name='fotp'),
    path('updatepass/',views.updatepass,name='pass'),
    path('change_done/',views.change_done,name='done'),
    path('registeration/',views.registeration),

]

