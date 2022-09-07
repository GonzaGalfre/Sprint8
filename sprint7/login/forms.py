from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    dni = forms.CharField(max_length=8)

    class Meta:
        model = User
        fields = ('username', 'dni', 'password1', 'password2', )