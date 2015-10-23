from django.shortcuts import render
from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name="profiles/profile.html"

class ProfileUpdateView(TemplateView):
    template_name="profiles/update_profile.html"
