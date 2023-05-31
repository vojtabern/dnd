from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *

def index(request):
    return render(request, "index.html", context=None)

class Region(ListView):
    model = Region
    ordering = ["nazev"]
    context_object_name = "regiony"
    template_name = "region/region.html"

class Stat(ListView):
    model = Stat
    ordering = ["region"]
    context_object_name = "staty"
    template_name = "stat/stat.html"

    # model = MyModel
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # Apply filtering logic
    #     filtered_queryset = queryset.filter(my_field='my_value')
    #     return filtered_queryset