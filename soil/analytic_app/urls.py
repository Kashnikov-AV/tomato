from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "analytic_app"
urlpatterns = [
    path("", views.AnalyticTemplateView.as_view(), name="index"),
]