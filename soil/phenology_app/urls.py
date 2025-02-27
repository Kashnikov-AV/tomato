from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "phenology_app"
urlpatterns = [
    path("", views.PhenologyTemplateView.as_view(), name="index"),
]