from django.db import models
import uuid
# Create your models here.

class BlogArticle(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
