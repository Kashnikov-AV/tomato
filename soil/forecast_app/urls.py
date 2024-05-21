from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "forecast_app"
urlpatterns = [
    path("", views.ForecastTemplateView.as_view(), name="index"),
]
