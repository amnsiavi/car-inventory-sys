from django.db import models
from datetime import datetime

# Create your models here.

def upload_to(instance,filename):
    return 'images/{filename}'.format(filename=filename)
class CarInventory(models.Model):

    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to=upload_to, blank=True, null=True)
    price = models.CharField(max_length=50)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())
    is_avaliable = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    