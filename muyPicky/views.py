import random
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import RestaurantLocation

# Create your views here.
def restaurant_listview(request):
    template_name = 'restaurants/restaurant_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name , context)
