from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import UserRegisterForm
from users.models import UserProfile


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html" 
    success_message = "You have successfully signed up!"
    
    def form_valid(self, form):
        response = super().form_valid(form)
       
        cleaned_data = form.cleaned_data
        profile = UserProfile(
            phone=cleaned_data["phone"],
            birth_day=cleaned_data['birth_day'],
            gender=cleaned_data['gender'],
            user=self.object
        )
        profile.save()
        
        return response
