from django.shortcuts import render, redirect
from .models import User

# context -> ინფორმაცია რომელიც გადაეცემა template ს დარენდერების დროს, render ის მე 3 არგუმენტი, ეგ არგუმენტი აუცილებლად უნდა იყოს dictionary
def all_users(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'users_index.html', context)

def delete_user(request, id):
    user_delete = User.objects.get(id=id)
    user_delete.delete()
    return redirect('main_users')

def register_user(request):
    if request.method == 'POST':
        
        email = request.POST.get('user_email')
        username = request.POST.get('user_name')
        age = request.POST.get('user_age')
        password = request.POST.get('password')
        
        new_user = User(username=username, age=age, email=email, password=password)
        new_user.save()
        
        return redirect('main_users')
    return render(request, 'users_registration.html')

def edit_user(request):
    
    return redirect('main_users')

def user_info(request, id):
    context = {
        'user_info' : User.objects.get(id=id)
    }
    return render(request, 'users_details.html', context)

def login_user(request):
    context = {
        'errors': []
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            found_user = User.objects.get(email=email, password=password)
            context['errors'] = []
            
            User.objects.update(is_current_user=False) # ყველა ოვიექტს შეუცვლის is_current_user ს
            
            found_user.is_current_user = True
            found_user.save()
        except:
            context['errors'] = ['invalid email or password']
    
    return render(request, 'users_login.html', context)

def user_profile(request):
    try:
        context = {
            'current_user' : User.objects.get(is_current_user=True)
        }
    except:
        context = {
            'current_user' : None
        }
    return render(request, 'users_profile.html', context)

def logout_user(request):
    User.objects.update(is_current_user=False)
    return redirect('main_users')