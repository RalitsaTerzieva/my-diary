from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import UserRegisterForm


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html" 
    success_message = "You have successfully signed up!"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Create an UserProfile instance and set the user foreign key to the user that we just created
        # self.object is the newly created User object
        return response
