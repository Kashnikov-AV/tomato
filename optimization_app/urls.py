from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "optimization_app"
urlpatterns = [
    path("", views.OptimizationTemplateView.as_view(), name="index"),
]