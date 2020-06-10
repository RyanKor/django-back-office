from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'last_name', 'username', 'password',)

    labels = {
        'email': (""),
        'last_name': (""),
        'username': (""),
        'password': (""),
    }

    widgets = {
        'email': forms.TextInput(attrs={'placeholder': "email"}),
        'last_name': forms.TextInput(attrs={'placeholder': "name"}),
        'username': forms.TextInput(attrs={"placeholder": "User ID"}),
        'password': forms.PasswordInput(attrs={"placeholder": "Password"}),
    }


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "username"}))
    password = forms.CharField(widget=PasswordInput(
        attrs={"placeholder": "Password"}))
