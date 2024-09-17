from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10 , decimal_places=3)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

def __str__(self):
    return self.firstname