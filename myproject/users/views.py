from django.shortcuts import render, redirect
from .utils import delete_account, login_account, logout_account, get_current_user, get_all_users, get_user_info, change_user
from .forms import RegisterForm, LoginForm, ProfileEditForm

# context -> ინფორმაცია რომელიც გადაეცემა template ს დარენდერების დროს, render ის მე 3 არგუმენტი, ეგ არგუმენტი აუცილებლად უნდა იყოს dictionary
def all_users(request):
    context = {
        'all_users': get_all_users()
    }
    return render(request, 'users_index.html', context)

def delete_user(request, id):
    delete_account(id=id)
    return redirect('main_users')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            return render(request, 'users_registration.html', {
                'register_form': form
            })

    context = {
        'register_form' : RegisterForm()
    }
    return render(request, 'users_registration.html', context)

def edit_user(request):
    try:
        context = {
            'current_user' : get_current_user(),
            'profile_edit_form': ProfileEditForm()
        }
    except:
        return redirect('user_login')

    if request.method == 'POST':
        change_user(request.POST)
        return redirect('user_profile')
        
    return render(request, 'users_edit.html', context)

def user_info(request, id):
    context = {
        'user_info' : get_user_info(id=id)
    }
    print(get_user_info(id=id))
    return render(request, 'users_details.html', context)

def login_user(request):
    if request.method == 'POST':
        try:
            login_account(request.POST)
            
            return redirect('main_users')
        except:
            return render(request, 'users_login.html', {
                'login_form' : LoginForm(),
                'errors' : ['Invalid username or password']
            })
    context = {
        'login_form' : LoginForm(),
        'errors' : []
    }
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
    logout_account()
    return redirect('main_users')