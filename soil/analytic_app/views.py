from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class AnalyticTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "analytic-page.html"