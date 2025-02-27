"""
URL configuration for soil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('signup_app.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name="index-page"),
    path('analytic/', include("analytic_app.urls", namespace="analytic")),
    path('forecast/', include("forecast_app.urls", namespace="forecast")),
    path('optimization/', include("optimization_app.urls", namespace="optimization")),
    path('phenology/', include("phenology_app.urls", namespace="phenology")),
    path('general/', include("general_forms_app.urls", namespace="general")),
]
