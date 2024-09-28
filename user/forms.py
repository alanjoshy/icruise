from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from user.models import Userdetails


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class Registrationform(forms.ModelForm):
    class Meta:
        model = Userdetails
        exclude = ('basic_data',)

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
