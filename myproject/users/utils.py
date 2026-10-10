from .models import User


def get_all_users():
    return User.objects.all()

def get_user_info(id):
    return User.objects.get(id=id)

def change_user(request_post, current_user):
    email = request_post.get('email')
    username = request_post.get('username')
    age = request_post.get('age')
    
    if email != '':
        current_user.email = email
        current_user.save()
    
    if username != '':
        current_user.username = username
        current_user.save()
        
    if age != '':
        current_user.age = age
        current_user.save()