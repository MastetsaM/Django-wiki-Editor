from django.contrib import admin
from django.db import models

# Register your models here.
class ok(models.Model):
    first_name = models.CharField(max_length=30)

admin.register(ok)

@admin.register(ok)
class OkAdmin(admin.ModelAdmin):
    first_name = models.CharField(max_length=30)
