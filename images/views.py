from django.shortcuts import render, redirect
from .models import Image

def upload_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        image_data = image_file.read()  # Read the binary data from the uploaded image
        Image.objects.create(binary_data=image_data)
        return redirect('receiver')
    return render(request, 'upload_image.html')

def display_image(request):
    images = Image.objects.all()
    return render(request, 'display_image.html', {'images': images})
