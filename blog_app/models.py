from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)  # default
    author = models.ForeignKey(User, on_delete=models.CASCADE)
