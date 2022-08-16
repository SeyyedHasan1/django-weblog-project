from django.shortcuts import render
from django.views.generic import CreateView
from .froms import CustomCreationForm
from django.urls import reverse_lazy
# Create your views here.


# class HomePageView(TemplateView):
#     template_name='accounts/home.html'

class SignUpView(CreateView):
    form_class=CustomCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'
