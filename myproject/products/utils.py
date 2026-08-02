from .models import Product
from users.models import User

def add_product(request_post):
    title = request_post.POST.get('title')
    price = request_post.POST.get('price')
    desc = request_post.POST.get('desc')
    rating = request_post.POST.get('rating')
    current_user_id = User.objects.get(is_current_user = True).id
    
    new_product = Product(title=title, price=price, desc=desc, rating=rating, user=current_user_id)
    new_product.save()

def delete_product(id):
    user_delete = Product.objects.get(id=id)
    user_delete.delete()

def get_all_products():
    return Product.objects.all()

def get_product_info(id):
    return Product.objects.get(id=id)