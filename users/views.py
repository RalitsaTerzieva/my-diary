from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import UserRegisterForm
from users.models import UserProfile
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView
    )
from entries.models import Entry


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

class UserProfileDetailsView(DetailView):
    model = UserProfile
    
    def get_object(self):
        return self.model.objects.get(user=self.request.user)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "entries_count": Entry.objects.filter(user=self.request.user).count(),
        })
         
        return context
    
    
    
class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = UserProfile
    fields = ["gender", "birth_day", "phone"]
    success_message = "Your user profile was updated!"
    
    def get_object(self):
        return self.model.objects.get(user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy("profile-details", kwargs={"pk": self.object.pk})