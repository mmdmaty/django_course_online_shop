from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'pages_home.html'

class AboutUsView(TemplateView):
    template_name = 'pages_AboutUs.html'