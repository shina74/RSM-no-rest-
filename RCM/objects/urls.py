from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'heroes', ObjectViewSet)


urlpatterns = [
    path('', Objects.as_view()),
    path('<int:pk>/', ObjectDetailView.as_view(), name='object_detail'),
    path('create_obj/', ObjectCreateView.as_view(), name='object_create'),
    path('create_house/', HouseCreateView.as_view(), name='house_create'),
    path('create/<int:pk>', ObjectUpdateView.as_view(), name='object_update'),
    path('delete/<int:pk>', ObjectDeleteView.as_view(), name='object_delete'),
]