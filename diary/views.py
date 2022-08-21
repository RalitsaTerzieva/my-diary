from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from entries.models import Entry


class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self):
        context = {
            "users_count": User.objects.all().count(),
            "entries_count": Entry.objects.all().count(),
        }
         
        return context