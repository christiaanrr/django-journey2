from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_category


class RestaurantLocation(models.Model):
    name        = models.CharField(max_length = 100)
    location    = models.CharField(max_length=100, null=True, blank=True)
    category    = models.CharField(max_length=100, null=True, blank=True, validators=[validate_category])
    description = models.TextField(default="")
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True, blank=True)

# shows name of restaurant in admin
    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)