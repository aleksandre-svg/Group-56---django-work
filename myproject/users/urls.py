from django.urls import path
from . import views


# user/ -> ყველა user ის ინფორმაცია
# user/delete -> user წაიშალა
# user/add -> user დაემატა
# user/edit -> user შეიცვალა


urlpatterns = [
    path('', views.all_users, name='main_users'),
    path('register/', views.register_user, name='add_user'),
    path('edit/', views.edit_user, name='edit_user'),
    path('<int:id>/', views.user_info, name='user_info'),
    path('login/', views.login_user, name='user_login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout_user, name='logout_user'),
    path('verification/', views.verify_user, name='verification')
]


