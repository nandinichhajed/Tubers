from django.db import models

# Create your models here.
class Contactinfo(models.Model):
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=100, blank=True)
    landmark = models.CharField(max_length=100, blank=True)
    town_or_city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.phone
    
class Socallinks(models.Model):
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    yt_link = models.CharField(max_length=255)
    
    def __str__(self):
        return self.fb_link