from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'input100', 'name': 'email', 'type': 'email'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'firstname'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'input100', 'name': 'lastname'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input100', 'name': 'password1'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input100', 'name': 'password2'})

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
