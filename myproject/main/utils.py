from .models import Review

def add_review(request_post):
    title = request_post.POST.get('title')
    review_text = request_post.POST.get('review_text')
    rating = request_post.POST.get('rating')
    
    new_review = Review(title=title, desc=review_text, rating=rating)
    new_review.save()

def get_all_reviews():
    return Review.objects.all()