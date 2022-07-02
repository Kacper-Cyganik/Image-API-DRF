from tkinter import Image
from xmlrpc.client import ResponseError
from rest_framework import generics
from .renderers import JPEGRenderer, PNGRenderer
from images.models import Image
from rest_framework.response import Response

class ImageAPIView(generics.RetrieveAPIView):

    renderer_classes = [JPEGRenderer]
    
    def get(self, request, *args, **kwargs):
        queryset = Image.objects.get(id=self.kwargs['id']).image
        data = queryset
        return Response(data, content_type='image/jpg')
