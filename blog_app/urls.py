from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_app-home'),
    path('about/', views.about, name='blog_app-about'),
]