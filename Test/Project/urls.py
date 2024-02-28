from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myWiki import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include('django_nyt.urls')),
    path("media/", views.upload_media, name="upload_media"),
    path('', include('wiki.urls')),

]
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)