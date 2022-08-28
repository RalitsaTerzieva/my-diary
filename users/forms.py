# TODO: Create a RegisterForm that subclasses django.contrib.auth.forms.UserCreationForm
# Add the fields that will be stored in UserProfile to that form

from random import choices
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import GENDER_CHOICES

class UserRegisterForm(UserCreationForm):
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES, widget=forms.Select(attrs={"class": "form-control", "autocomplete": "off", "required": "true"}))
    phone = forms.CharField(label="Phone", widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off", "required": "true"}))
    birth_day = forms.DateField(label="Gender", widget=forms.SelectDateWidget(attrs={"class": "form-control", "autocomplete": "off", "required": "true", "style": "width: 30%; margin-right:10px; display: inline-block"}))