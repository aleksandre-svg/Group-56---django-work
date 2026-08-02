from django.shortcuts import render, redirect
from .utils import register_user, delete_user, login_user, logout_user, get_current_user, get_all_users, get_user_info, edit_user

# context -> ინფორმაცია რომელიც გადაეცემა template ს დარენდერების დროს, render ის მე 3 არგუმენტი, ეგ არგუმენტი აუცილებლად უნდა იყოს dictionary
def all_users(request):
    context = {
        'all_users': get_all_users()
    }
    return render(request, 'users_index.html', context)

def delete_user(request, id):
    delete_user(id=id)
    return redirect('main_users')

def register_user(request):
    if request.method == 'POST':
        register_user(request.POST)
        return redirect('user_login')
    return render(request, 'users_registration.html')

def edit_user(request):
    try:
        context = {
            'current_user' : get_current_user()
        }
    except:
        return redirect('user_login')

    if request.method == 'POST':
        edit_user(request.POST)
        return redirect('user_profile')
        
    return render(request, 'users_edit.html', context)

def user_info(request, id):
    context = {
        'user_info' : get_user_info(id=id)
    }
    return render(request, 'users_details.html', context)

def login_user(request):
    context = {
        'errors': []
    }
    if request.method == 'POST':
        try:
            login_user(request.POST)
            context['errors'] = []
            
            return redirect('main_users')
        except:
            context['errors'] = ['invalid email or password']
    
    return render(request, 'users_login.html', context)

def user_profile(request):
    try:
        context = {
            'current_user' : get_current_user()
        }
    except:
        context = {
            'current_user' : None
        }
    return render(request, 'users_profile.html', context)

def logout_user(request):
    logout_user()
    return redirect('main_users')