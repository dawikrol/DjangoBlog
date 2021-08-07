from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView


def home(request):
	context = {
		'posts': Post.objects.all(),
	}
	return render(request, 'blog_app/home.html', context)


class PostListView(ListView):
	# class as view (home)
	model = Post
	template_name = 'blog_app/home.html'  # we need to change default name of view <app>/<model>_view_type>.html
	context_object_name = 'posts'  # we need to change default context name
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog_app/post_details.html'



def about(request):
	return render(request, 'blog_app/about.html')
