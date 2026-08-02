from django.shortcuts import render, redirect
from .utils import add_review, get_all_reviews
# Create your views here.
def main(request):
    context = {
        'all_reviews' : get_all_reviews()
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    if request.method == 'POST':
        add_review(request.POST)
        return redirect('main_page')
    return render(request, 'services.html')