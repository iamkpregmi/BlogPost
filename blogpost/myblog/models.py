from django.db import models
from tinymce.models import HTMLField

class myblog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_desc = HTMLField()
