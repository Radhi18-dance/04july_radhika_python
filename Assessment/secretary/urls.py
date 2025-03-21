from django.contrib import admin
from django.urls import path,include
from secretary import views


urlpatterns = [
    path('add/',views.add),
    path('otpapp/',views.otpapp,name='otpverify'),

   

]