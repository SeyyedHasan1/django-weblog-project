from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        # fields=UserCreationForm.Meta.fields + ('age',)  #add the age model that was created in models.py
        fields=('username','email','age')  #add email address to sign up fields .*password add automaticly
        

class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=CustomUser
        fields=UserChangeForm.Meta.fields