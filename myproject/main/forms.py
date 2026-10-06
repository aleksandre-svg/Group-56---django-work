from django import forms
# <label for="title">review title: </label><br>
# <input type="text" name="title" id="title"><br><br>

# <label for="review_text">review: </label><br>
# <textarea name="review_text" id="review_text"></textarea><br><br>

# <label for="rating">rating (1-5): </label><br>
# <input type="number" name="rating" id="rating"><br><br>

class ReviewForm(forms.Form):
    title = forms.CharField()
    review_text = forms.CharField()
    rating = forms.IntegerField()