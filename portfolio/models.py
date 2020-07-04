from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/', height_field=None, width_field=None, max_length=100)
    url = models.URLField(blank=True)
    objects = models.Manager()
