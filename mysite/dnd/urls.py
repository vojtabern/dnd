from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("regiony/", views.Region.as_view(), name="regiony"),
    path("staty/", views.Stat.as_view(), name="staty"),
]