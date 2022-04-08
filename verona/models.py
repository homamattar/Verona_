from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)

    # main_photo = models.ImageField(upload_to='main_pics/%Y/%m/%d/', blank=True)
    main_photo = ResizedImageField(size=[500, 500], quality=100,crop=['middle', 'center'], upload_to='main_pics/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)

    def __str__(self):
        if self.featured:
            return "⭐ {}".format(self.name)
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    msg = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')
    

    def __str__(self):
        return self.name


