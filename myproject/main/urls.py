from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main_page'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_page'),
    path('services/', views.services, name='services_page')
]
