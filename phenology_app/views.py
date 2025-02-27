from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class PhenologyTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "phenology-page.html"
