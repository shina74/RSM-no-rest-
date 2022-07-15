from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator

from .models import House, Room, Place, Object, Category
from .filters import ObjectFilter
from .forms import ObjectForm, HouseForm

from rest_framework import viewsets

from .serializers import ObjectSerializer
from .models import House, Room, Place, Object, Category


class Objects(ListView):
    model = Object
    template_name = 'object_list.html'
    context_object_name = 'objects'
    ordering = ["name"]
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ObjectFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ObjectDetailView(DetailView):
    template_name = 'object_detail.html'
    queryset = Object.objects.all()


class ObjectCreateView(CreateView):
    template_name = 'object_create.html'
    form_class = ObjectForm


class ObjectUpdateView(UpdateView):
    template_name = 'object_create.html'
    form_class = ObjectForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Object.objects.get(pk=id)


class ObjectDeleteView(DeleteView):
    template_name = 'object_delete.html'
    queryset = Object.objects.all()
    success_url = '/objects/'


class HouseCreateView(CreateView):
    template_name = 'object_create.html'
    form_class = HouseForm


# Rest API


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all().order_by('name')
    serializer_class = ObjectSerializer
