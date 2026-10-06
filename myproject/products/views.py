from django.shortcuts import redirect, render
from .utils import delete_product, get_all_products, get_product_info
from users.utils import get_current_user, get_user_info
from .forms import ProductAddForm

# Create your views here.
def all_products(request):
    context = {
        'all_products' : get_all_products()
    }
    return render(request, 'products_index.html', context)

def delete_product(request, id):
    delete_product(id=id)
    return redirect('all_products')

def add_product(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = get_current_user().id
            product.save()
            
        else:
            return render(request, 'add_product.html', {
                'product_add_form': ProductAddForm(),
                'error': 'invalid info'
            })
        return redirect('all_products')
    return render(request, 'add_product.html', {
        'product_add_form': ProductAddForm()
    })

def edit_product(request):
    return redirect('all_products')

def product_details(request, id):
    found_product = get_product_info(id=id)
    context = {
        'product_detail' : found_product,
        'product_holder' : get_user_info(id=found_product.id),
        'current_user' : get_current_user()
    }
    return render(request, 'product_details.html', context)