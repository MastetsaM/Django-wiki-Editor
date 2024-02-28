from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse

import os
# Create your views here.
@csrf_exempt
def upload_media(request):
    file_obj = request.FILES['media']
    
    file_path = os.path.join(settings.MEDIA_ROOT, file_obj.name)

    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

    return HttpResponse("ok")