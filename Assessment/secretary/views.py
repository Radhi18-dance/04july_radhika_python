from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
import random
from assessment import settings 
from django.contrib import messages

# Create your views here.

otp=0
def add(request):
    msg=""
    if request.method=='POST':
        global newadd
        newadd=signupForm(request.POST)
        if newadd.is_valid():
          
             # Send OTP
            global otp
            otp=random.randint(11111,99999)
            sub="Your One Time Password"
            msg=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nHOUSING SOCIETY- Rajkot\nFOR CONTACT +8866399207|"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            print("Mail send successfully!")
            return redirect("otpverify")
        else:
            print(newadd.errors)
            msg="error"
        
    return render(request,'add.html',{'msg':msg})

def otpapp(request):
    msg=""
    global otp
    global newadd
    print(otp)
    if request.method=="POST":
        if request.POST["myotp"]==str(otp):
            newadd.save()

            print("Verification Successfully!")
            return redirect('/')
        else:
            print("OTP ERROR!")
    return render(request,'otpapp.html',{'msg':msg})

