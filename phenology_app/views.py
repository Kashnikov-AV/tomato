from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, BaseCreateView
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Tk, Plant, Record, Block
from .forms import RecordForm, NumberPlantForm
from django.urls import reverse_lazy

# Create your views here.
class PhenologyTemplateView(LoginRequiredMixin, ListView):
    template_name = "phenology/phenology-page.html"
    model = Tk


class TkListView(LoginRequiredMixin, ListView):
    template_name = 'phenology/phenology-page.html'
    model = Tk


class BlockListView(ListView):
    template_name = 'phenology/blocks_list.html'
    model = Block

    def get_queryset(self):
        return Block.objects.filter(tk__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = self.get_queryset()
        context['object_list'] = object_list
        context['pk'] = self.kwargs['pk']
        context['tk'] = Tk.objects.get(pk=self.kwargs['pk'])
        return context


class PlantListView(FormMixin, ListView):
    template_name = 'phenology/plants_list.html'
    model = Plant
    form_class = NumberPlantForm
    success_url = 'phenology:plants-list'

    def get_queryset(self):
        return Plant.objects.filter(block__tk=self.kwargs['pk'], block__key=self.kwargs['block'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = self.get_queryset()
        context['object_list'] = object_list
        context['pk'] = self.kwargs['pk']
        context['block_'] = self.kwargs['block']
        context['tk'] = Tk.objects.get(pk=self.kwargs['pk'])
        return context


def createPlants(request, block, tk):
    if request.method=='POST':
        number_of_plants = request.POST.get('number_of_plants')
        block_id = int(block)
        block_obj = Block.objects.get(pk=block_id)

    # Создание растений
    for key in range(int(number_of_plants)):
        plant = Plant(key=key+1, block=block_obj)
        plant.save()

    return redirect('phenology:plants-list', pk=tk, block=block)


class RecordCreateView(CreateView):
    template_name = 'phenology/record_create.html'
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('phenology:index')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.plant = Plant.objects.get(key=self.kwargs['plant'],
                                              block__key=self.kwargs['block'],
                                              block__tk=self.kwargs['pk'],
                                              )
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RecordCreateView, self).get_context_data(*args, **kwargs)
        context['pk'] = self.kwargs['pk']
        context['block_'] = self.kwargs['block']
        context['plant'] = self.kwargs['plant']
        context['tk'] = Tk.objects.get(pk=self.kwargs['pk'])
        return context


class RecordListView(ListView):
    model = Record
    template_name = 'phenology/records_list.html'

    def get_queryset(self):
        return Record.objects.filter(plant__block__tk=self.kwargs['pk'], plant__block__key=self.kwargs['block'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = self.get_queryset()
        context['object_list'] = object_list
        context['pk'] = self.kwargs['pk']
        context['block_'] = self.kwargs['block']
        context['tk'] = Tk.objects.get(pk=self.kwargs['pk'])
        context['kwargs'] = self.kwargs
        return context



