from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
    
class Editor1(models.Model):
    name = models.CharField(max_length=50, null=True)
    ckeditor = RichTextField(null=True)
    django_embed_video = EmbedVideoField(null=True)
    video = models.FileField(upload_to='media/', null=True)
    
    def __str__(self):
        return self.name
    
    
    