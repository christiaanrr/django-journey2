from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import RestaurantLocation

# Create your views here.
def restaurant_listview(request):
    template_name = 'restaurants/restaurant_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    template_name = 'restaurants/restaurant_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

