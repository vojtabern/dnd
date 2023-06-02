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

class Mesto(ListView):
    model = Mesto
    ordering = ["stat_nazev"]
    context_object_name = "mesta"
    template_name = "mesta/mesta.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spravci'] = Spravce.objects.select_related('spravce', 'mesto')
        return context

class NPCs(ListView):
    model = NPC
    ordering = ["prijmeni"]
    context_object_name = "NPCs"
    template_name = "NPC/npcs.html"

class Npc(DetailView):
    model = NPC
    context_object_name = "NPC"
    template_name = "NPC/npcDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        npc = self.get_object()
        context['spravci'] = Spravce.objects.filter(spravce=npc)
        context['vladce'] = VladceStatu.objects.filter(vladce=npc)
        context['stattable'] = StatTable.objects.filter(npc=npc)
        context['actions'] = Actions.objects.filter(npc=npc)
        return context

class NpcPrint(DetailView):
    model = NPC
    context_object_name = "NPC"
    template_name = "NPC/printable.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        npc = self.get_object()
        context['spravci'] = Spravce.objects.filter(spravce=npc)
        context['vladce'] = VladceStatu.objects.filter(vladce=npc)
        context['stattable'] = StatTable.objects.filter(npc=npc)
        context['actions'] = Actions.objects.filter(npc=npc)
        return context

    # model = MyModel
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # Apply filtering logic
    #     filtered_queryset = queryset.filter(my_field='my_value')
    #     return filtered_queryset