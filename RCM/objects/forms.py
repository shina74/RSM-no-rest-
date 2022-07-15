from django.forms import ModelForm
from .models import *


class ObjectForm(ModelForm):
    class Meta:
        model = Object
        fields = ['name', 'description', 'category', 'place']


class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ['name', 'description']
