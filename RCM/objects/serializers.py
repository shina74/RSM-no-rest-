from rest_framework import serializers

from .models import House, Room, Place, Object, Category


class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = ('name',
                  'description',
                  'creation_date',
                  'changes_date',
                  'photo',
                  'place',
                  'favorite'
                  'category')
