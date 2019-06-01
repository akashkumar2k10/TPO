from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


# *************
# User Signup Form
# *************
class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2',)


# *************
# Profile Signup Form
# *************
class SignUpFormProfile(forms.ModelForm):
    birth_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'placeholder': 'yyyy-mm-dd'}),
        )
    class Meta:
        model = Profile
        fields = ( 'birth_date', 'gender', )

