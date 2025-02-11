from django.shortcuts import render
from user.forms import CustomUserCreationForm
from django.views import generic
from user.models import CustomUserModel
from django.urls import reverse_lazy


class signup(generic.CreateView):
    model = CustomUserModel
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('home')
