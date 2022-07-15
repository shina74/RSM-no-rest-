from django_filters import FilterSet
from .models import *


class ObjectFilter(FilterSet):
    class Meta:
        model = Object
        fields = ('name', 'description', 'category', 'place')