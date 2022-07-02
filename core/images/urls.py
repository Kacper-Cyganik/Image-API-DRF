from re import template
from django.urls import path
from django.views.generic import TemplateView
from .views import ImageListView

app_name = 'images'

urlpatterns = [
    path('', TemplateView.as_view(template_name='images/index.html')),
    path('all/', ImageListView.as_view(), name='all_images'),
]
