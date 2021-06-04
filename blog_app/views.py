from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
	{
		'author': 'Dawid',
		'title': 'Post1',
		'content': 'Cooooooooooooooooooooooooooooooooooontent',
		'date': 'May 20, 2020',
	},
	{
		'author': 'Dawid',
		'title': 'Post1',
		'content': 'Cooooooooooooooooooooooooooooooooooontent',
		'date': 'May 20, 2020',
	},

]


def home(request):
	context = {
		'posts': posts,
	}
	return render(request, 'blog_app/home.html', context)


def about(request):
	return render(request, 'blog_app/about.html')
