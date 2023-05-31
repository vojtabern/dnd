from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

def index(request):
    return render(request, "index.html", context=None)
# Create your views here.


class MyListView(ListView):
    pass
    # model = MyModel
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # Apply filtering logic
    #     filtered_queryset = queryset.filter(my_field='my_value')
    #     return filtered_queryset