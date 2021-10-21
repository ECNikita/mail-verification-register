import random
from accounts.models import Profile
from django.shortcuts import redirect, render
from accounts.databaseProvider.userCRUD import *
from django.contrib import messages
#from .models import *

from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request , 'home.html')
    return redirect('/saveapp')



def login_attempt(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = Validate_user(email,password)
        print(user_obj)
        

        if user_obj is None:
            messages.success(request, 'Email or Password is Wrong.')
            return redirect('/accounts/login')
        
        print(user_obj)
        if user_obj["IsActive"] == False:
            messages.success(request, 'Profile is not activated.')
            return redirect('/accounts/login')
        
        request.session['uid'] = user_obj["uid"]
        return redirect('/saveapp/insertapp')

    return render(request , 'login.html')

def register_attempt(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if Check_user_already_register(email):
                messages.success(request, 'Email is already taken.')
                return redirect('/register')

            
            auth_token = random.randint(10000,99999)
            Register_user(email,password,auth_token)

            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)


    return render(request , 'register.html')

def success(request):
    return render(request , 'success.html')



def token_send(request):
    return render(request , 'token_send.html')



def verifyotp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
    
        if Verify_user(email,otp) == False:
            messages.success(request, 'Email or OTP is Wrong.')
            return redirect('/accounts/verifyotp')
        
        Activate_user(email)
        return redirect('/accounts/login')
        
    
    return render(request , 'otp.html')


def error_page(request):
    return  render(request , 'error.html')








def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'please enter this otp on activation page : {token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    