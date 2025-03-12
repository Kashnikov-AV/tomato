from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "phenology_app"
urlpatterns = [
    path("", views.PhenologyTemplateView.as_view(), name="index"),
    path('tk/<int:pk>/blocks/', views.BlockListView.as_view(), name='blocks-list'),
    path('tk/<int:pk>/block/<int:block>/plants/', views.PlantListView.as_view(), name='plants-list'),
    path('create-plant/<int:block>/<int:tk>/', views.createPlants, name='create-plants'),
    path('tk/<int:pk>/block/<int:block>/plants/records/', views.RecordListView.as_view(), name='records-list'),
    path('tk/<int:pk>/block/<int:block>/plant/<int:plant>/record/create/', views.RecordCreateView.as_view(), name='record-create'),
]