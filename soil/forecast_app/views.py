from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ForecastTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "forecast-page.html"