from django.forms import ModelForm
from .models import Brands
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrandsForm(ModelForm):
    class Meta:
        model = Brands
        fields = '__all__'

class CreateNewUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']