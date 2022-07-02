from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return f'images/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    options = (
        ('active','Active'),
        ('deactivated','Deactivated'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    alt = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=user_directory_path, default='post/default.jpg')
    slug = models.SlugField(max_length=255, unique_for_date='created')
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    status = models.CharField(max_length=12, choices=options, default='active')
    

