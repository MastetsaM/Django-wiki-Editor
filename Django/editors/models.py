from django.db import models

from django import forms
from tinymce.models import HTMLField  
  
  
class Article(models.Model): 
    title = models.CharField(max_length=300, null=True, blank=True)
    content = HTMLField()

    def __str__(self):
        return self.title


 