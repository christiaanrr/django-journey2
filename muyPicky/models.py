from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    name        = models.CharField(max_length = 100)
    location    = models.CharField(max_length=100, null=True, blank=True)
    category    = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="")
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

# shows name of restaurant in admin
    def __str__(self):
        return self.name
