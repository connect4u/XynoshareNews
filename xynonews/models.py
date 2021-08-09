from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    economy = models.BooleanField(default=False)
    international = models.BooleanField(default=False)
    technology = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    img = models.ImageField(upload_to='pics')
    short_description = models.CharField(max_length=400, default='')
    trend = models.BooleanField(default=False)

  