from django.shortcuts import render, redirect
from . models import Review

# Create your views here.
def main(request):
    context = {
        'all_reviews' : Review.objects.all()
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')
        
        new_review = Review(title=title, desc=review_text, rating=rating)
        new_review.save()
        
        return redirect('main_page')
    
    return render(request, 'services.html')