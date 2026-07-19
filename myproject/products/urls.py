from django.urls import path
from . import views

# products/ -> გამოჩნდეს ყველა პროდუქტი (needs front end)
# products/delete -> წაიშალოს პროდუქტი (doesn't need front end)
# products/add -> დაემატოს პროდუქტი  (doesn't need front end)
# products/edit -> შეიცვალოს პროდუქტი (doesn't need front end)

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('add/', views.add_product, name='add_product'),
    path('edit/', views.edit_product, name='edit_product'),
    path('<int:id>/', views.product_details, name='product_detail')
]
