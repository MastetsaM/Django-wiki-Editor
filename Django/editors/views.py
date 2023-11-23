from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    editors = Editor1.objects.all
    return render(request, "index.html", context={"editors": editors})