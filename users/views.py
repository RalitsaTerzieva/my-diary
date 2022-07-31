from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html" 
    success_message = "You have successfully signed up!"
 