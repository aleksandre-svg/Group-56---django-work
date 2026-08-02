from .models import User

def register_user(request_post):
    new_user = User(username=request_post.get('user_name'), 
                    age=request_post.get('user_age'), 
                    email=request_post.get('user_email'), 
                    password=request_post.get('user_password'))
    new_user.save()

def delete_user(id):
    User.objects.get(id=id).delete()

def login_user(request_post):
    found_user = User.objects.get(email=request_post.get('email'), password=request_post.get('password'))
    
    User.objects.update(is_current_user=False) # ყველა ოვიექტს შეუცვლის is_current_user ს
    
    found_user.is_current_user = True
    found_user.save()
    
def logout_user():
    User.objects.update(is_current_user=False)

def get_current_user():
    return User.objects.get(is_current_user = True)

def get_all_users():
    return User.objects.all()

def get_user_info(id):
    return User.objects.get(id=id)

def edit_user(request_post):
    email = request_post.get('user_email')
    username = request_post.get('user_name')
    age = request_post.get('user_age')
    password = request_post.get('password')
    
    current_user = User.objects.get(is_current_user = True)
    
    if email != '':
        current_user.email = email
        current_user.save()
    
    if username != '':
        current_user.username = username
        current_user.save()
        
    if age != '':
        current_user.age = age
        current_user.save()
    
    if password != '':
        current_user.password = password
        current_user.save()