from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('add/', views.add_product, name='add_product'),
    path('<int:id>/', views.product_details, name='product_detail')
]
