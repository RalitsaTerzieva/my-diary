# TODO: Create a RegisterForm that subclasses django.contrib.auth.forms.UserCreationForm
# Add the fields that will be stored in UserProfile to that form

from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="First Name")