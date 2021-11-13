from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100, blank=True)
    subject = models.TextField()
    message = models.TextField()
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.company_name