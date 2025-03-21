from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from .models import *
from django.core.mail import send_mail
import random
from assessment import settings 
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
def userlogin(request):
    msg=""
    if request.method=='POST':
        email=request.POST['email']
        pas=request.POST['password']

        user=signmodel.objects.filter(email=email,password=pas)
        uid=signmodel.objects.get(email=email)
        print("UserID:",uid.id)
        if user:
            print("Login Successfully!")
            msg="Login Successfully!"
            request.session['cuser']=email
            request.session['uid']=uid.id
            return redirect('/')
        else:
            print("Error...Login failed!")
            msg="Error...Login failed!"
    return render(request,'userlogin.html',{'msg':msg})

def usersignup(request):
    msg=""
    if request.method=='POST':
        global newReq
        newReq=signupForm(request.POST)
        email=""
        if newReq.is_valid():
            email=newReq.cleaned_data.get('email')
            try:
                signmodel.objects.get(email=email)
                print("email already exists")
                msg="EMAIL ALREADY EXISTS"
            except signmodel.DoesNotExist:
                #Email Sending Code
                global otp
                otp=random.randint(11111,99999)
                sub="Your One Time Password"
                msg=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nHOUSING SOCIETY- Rajkot\nFOR CONTACT +8866399207|"
                from_ID=settings.EMAIL_HOST_USER
                to_ID=[request.POST['email']]
                send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                print("Mail send successfully!")
                
                #send_mail(subject="Your One Time Password",message=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Tech - Rajkot\n+91 97247 99469 | sanket@tops-int.com",from_email=settings.EMAIL_HOST_USER,recipient_list=['kishantoliya4@gmail.com','meetladva1684@gmail.com','kevalkotadiya509@gmail.com','pratixagoswami2000@gmail.com','k.p.jogi89@gmail.com','radhikapithadia123@gmail.com'])
                return redirect('otpverify')
        else:
            print(newReq.errors)
            msg="error .....same email not allowed "
    return render(request,'usersignup.html',{'msg':msg})
def userlogut(request):
    logout(request)
    return redirect('/')

def otpverifcation(request):
    msg=""
    global otp
    global newReq
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            newReq.save()
            print("verification done")
            msg="verified........"
            return redirect('userlogin')
        else:
            print("error inavlid otp")
            msg="error invalid otp"
    return render(request,'otpverification.html',{'msg':msg})
def base(request):
    user=request.session.get('cuser')
    return render(request,'base.html',{'user':user})

def dashboard(request):
    user=request.session.get('cuser')
    return render(request,'dashboard.html')

def events(request):
    user=request.session.get('cuser')
    return render(request,'events.html')

def myprofile(request):
    msg=""
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=signmodel.objects.get(id=uid)
    if request.method=='POST':
        updateReq=updateform(request.POST,instance=cuser)
        if updateReq.is_valid():
            updateReq.save()
            
            print("Your profile has been updated!")
            msg="Your profile has been updated!"
            return redirect('/')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong...Try again!MAYBE FIELDS ARE SKIPPED....."
    return render(request,'myprofile.html',{'user':user,'cuser':cuser,'msg':msg})
    

def notice(request):
    user=request.session.get('cuser')
    return render(request,'notice.html')

def society_members(request):
    user=request.session.get('cuser')
    stdata=signmodel.objects.all()
    return render(request,'society_members.html',{'stdata':stdata})

def society_watchmen(request):
    user=request.session.get('cuser')
    stdata=signmodel.objects.all()
    return render(request,'society_watchmen.html',{'stdata':stdata})
def forgotpass(request):
    global otp
    msg=""
    if request.method=='POST':
        mail=request.POST['email']
        #smail=request.session['smail']=mail
        d=signmodel.objects.filter(email=mail)
        if d:
            global otp
            otp=random.randint(11111,99999)
            sub="Your One Time Password"
            msg=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nHOUSING SOCIETY- Rajkot\nFOR CONTACT +8866399207|"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            return redirect('fotp')
    return render(request,'forgotpass.html',{'msg':msg})
def fotpverify(request):
    msg=""
    global otp
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            
            print("verification done")
            msg="verified........"
            return redirect('pass')
        else:
            print("error inavlid otp")
            msg="error invalid otp"
    return render(request,'fotpverify.html',{'msg':msg})

def updatepass(request):
    msg=""
    
    user=request.session.get('cuser')
    print(user)
    if request.method == 'POST':
        data=signmodel.objects.get(email=user)

        fpas=updatepassForm(request.POST,instance=data)
        if fpas.is_valid():
            fpas.save()
            print("changed")
            msg="password updated"
            
            return redirect('done')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the error below.')
            msg="something wemt wrong"
    
    return render(request, 'updatepass.html',{'msg':msg,'user':user})

def change_done(request):
    return render(request,'change_done.html')

def registeration(request):
    msg=""
    user=request.session.get('cuser')
    if request.method=='POST':
        newCont=registerForm(request.POST)
        if newCont.is_valid():
            newCont.save()
            print("Your response has been submitted!")
            sub="register success"
            msg=f"Hello User!\n\nThanks for registration with us!\n\n\nThanks & Regards!\nHOUSING SOCIETY- Rajkot\nFOR CONTACT +8866399207|"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[newCont.cleaned_data['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            return redirect('/')
        else:
           print("error")

           msg="invalid"
    return render(request,'registeration.html',{'user':user,'msg':msg})
