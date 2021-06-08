from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()  #  save user in database
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('blog_app-home')
	else:
		form = UserRegisterForm(request.POST)
	return render(request, 'users_app/register.html', {'form': form})