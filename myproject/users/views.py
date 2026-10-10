from django.shortcuts import render, redirect
from .utils import get_all_users, get_user_info, change_user
from .forms import RegisterForm, LoginForm, ProfileEditForm
from .models import User
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

# context -> ინფორმაცია რომელიც გადაეცემა template ს დარენდერების დროს, render ის მე 3 არგუმენტი, ეგ არგუმენტი აუცილებლად უნდა იყოს dictionary
def all_users(request):
    return render(request, 'users_index.html', {
        'all_users': get_all_users()
    })

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        verification_code = ''
        alp = 'qwertyuiopasdfghjklmzxcvbnm1234567890'
        for i in range(6):
            verification_code += alp[random.randint(0, len(alp)-1)]
        
        if form.is_valid():
            request.session['verification_code'] = verification_code
            request.session['user_info'] = form.cleaned_data
            
            send_mail(
                subject='verification code',
                message=f"Your verification code is {verification_code}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data.get('email')]
            )
            
            return redirect('verification')
        else:
            return render(request, 'users_registration.html', {
                'register_form': form
            })

    return render(request, 'users_registration.html', {
        'register_form' : RegisterForm()
    })

def edit_user(request):
    if request.method == 'POST':
        change_user(request.POST, current_user = request.user)
        return redirect('user_profile')
    return render(request, 'users_edit.html', {
        'profile_edit_form': ProfileEditForm()
    })

def user_info(request, id):
    return render(request, 'users_details.html', {
        'user_info' : get_user_info(id=id)
    })

def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST.get('username'), password = request.POST.get('password'))
        if user:
            login(request, user)
        else:
            return render(request, 'users_login.html', {
                'login_form' : LoginForm(),
                'errors' : ['Invalid username or password']
            })
    return render(request, 'users_login.html', {
        'login_form' : LoginForm(),
        'errors' : []
    })

def user_profile(request):
    return render(request, 'users_profile.html')

def logout_user(request):
    logout(request)
    return redirect('main_users')

def verify_user(request):
    verification_code = request.session.get('verification_code')
    user_info = request.session.get('user_info')
    
    if 'user_verification_input' in request.GET:
        if request.GET.get('user_verification_input') == verification_code:
            User.objects.create_user(username = user_info.get('username'), email = user_info.get('email'), password = user_info.get('password'), age = user_info.get('age'))
            return redirect('user_login')
        else:
            return render(request, 'user_verification.html', {
                'error': 'incorrect code'
            })
    return render(request, 'user_verification.html')