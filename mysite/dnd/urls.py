from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("regiony/", views.Region.as_view(), name="regiony"),
    path("staty/", views.Stat.as_view(), name="staty"),
    path("mesta/", views.Mesto.as_view(), name="mesta"),
    path("npcs/", views.NPCs.as_view(), name="npcs"),
    path("npcs/npc/<int:pk>", views.Npc.as_view(), name="npcDetail"),
    path("npcs/npc/<int:pk>/printable", views.NpcPrint.as_view(), name="npcPrint"),
]