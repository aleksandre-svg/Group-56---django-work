from django import forms
from .models import Product

# <label for="title">title:</label><br>
# <input type="text" name="title" id="title"><br><br>

# <label for="price">price:</label><br>
# <input type="number" name="price" id="price"><br><br>

# <label for="desc">desc:</label><br>
# <input type="text" name="desc" id="desc"><br><br>

# <label for="rating">rating (1-5):</label><br>
# <input type="number" name="rating" id="rating"><br><br>

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'desc', 'rating')