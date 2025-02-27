from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class GeneralFormTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "general-form-page.html"
