from django.contrib import admin
from .models import House, Room, Place, Object, Category

admin.site.register(House)
admin.site.register(Room)
admin.site.register(Place)
admin.site.register(Object)
admin.site.register(Category)

