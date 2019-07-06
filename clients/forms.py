from django.forms import ModelForm
from django import forms
from .models import Client
from django.contrib.auth.models import User


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['nome','telefone','logradouro','bairro','numero','cidade','estado','país','cep']

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
        help_texts = {
            'username': ''
        }
