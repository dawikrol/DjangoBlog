from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:  # this class give nested name space for configuration
		model = User
		fields = ['username', 'email', 'password', 'password2']
