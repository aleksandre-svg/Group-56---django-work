from .models import Product
from users.utils import get_current_user

def delete_product(id):
    user_delete = Product.objects.get(id=id)
    user_delete.delete()

def get_all_products():
    return Product.objects.all()

def get_product_info(id):
    return Product.objects.get(id=id)