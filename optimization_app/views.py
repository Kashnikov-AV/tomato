from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class OptimizationTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "optimization-page.html"