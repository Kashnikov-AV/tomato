from django.urls import path
from . import views

app_name = "general_forms_app"
urlpatterns = [
    path("", views.GeneralFormTemplateView.as_view(), name="index"),
]
