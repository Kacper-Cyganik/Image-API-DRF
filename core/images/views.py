from django.views.generic import ListView
from .models import Category, Image

class ImageListView(ListView):
    model = Image
    template_name = 'images/all_images.html'

