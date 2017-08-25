from django import forms

from muyPicky.models import RestaurantLocation
from .models import Item

class ItemForm(forms.ModelForm):

    def __init__(self, user=None, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user)

    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]