from django.shortcuts import redirect, render
from .models import Product

# Create your views here.
def all_products(request):
    context = {
        'all_products' : Product.objects.all()
    }
    return render(request, 'products_index.html', context)

def delete_product(request, id):
    user_delete = Product.objects.get(id=id)
    user_delete.delete()
    return redirect('all_products')

def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        rating = request.POST.get('rating')
        
        new_product = Product(title=title, price=price, desc=desc, rating=rating)
        new_product.save()
        
        return redirect('all_products')
    
    return render(request, 'add_product.html')

def edit_product(request):
    return redirect('all_products')

def product_details(request, id):
    context = {
        'product_detail' : Product.objects.get(id=id)
    }
    return render(request, 'product_details.html', context)