import random
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
# function based view


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = random.randint(0, 1000000)
        some_list = ['yo', 'hey', 'hoy']
        htmlContent = {
            'html_var': True,
            'num': num,
            'some_list': some_list,
        }
        return htmlContent

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
