from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    phone_number = forms.CharField(required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    bank_card = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'bank_card', 'avatar']

