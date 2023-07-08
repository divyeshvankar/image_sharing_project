from django.urls import path
from images.views import upload_image, display_image
from django.contrib import admin


   

urlpatterns = [
    path('upload/', upload_image, name='uploader'),
    path('display/', display_image, name='receiver'),
    path('admin/', admin.site.urls),
]


