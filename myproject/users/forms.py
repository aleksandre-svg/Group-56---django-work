from django import forms
from .models import User

# Meta Class -> გვეხმარება იმაში რომ მონაცემთა ბაზის მოდელიდან გამომდინარე შევქმნათ form ის მოდელი

class RegisterForm(forms.ModelForm): # როცა form ი არი შექმნილი მოდელიდან გამომდინარე, უნდა მივუთითოთ ModelForm ი
    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={
                'style': 'color: red;'
            })
        }
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        for char in username:
            if char in '0123456789@#$':
                raise forms.ValidationError("username shouldn't contain numbers or symbols")
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if email.split('@')[1] != 'gmail.com':
            raise forms.ValidationError("email should end with gmail.com")
        
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) < 8:
            raise forms.ValidationError("password should be at least 8 characters long")
        
        count = 0
        
        for char in password:
            if char in '0123456789':
                count += 1
        
        if count < 1:
            raise forms.ValidationError("password should contain at least 1 number")
        
        return password

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={
                'style': 'color: red;'
            })
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={
                'style': 'color: red;'
            })
        }