from django import forms
from .models import Tk, Plant, Record
from datetime import date
from crispy_forms.helper import FormHelper


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['growth_per_week',
                  'stem_diameter',
                  'leaf_length',
                  'leaf_width',
                  'number_of_leaves_per_stem',
                  'internode_length',
                  ]
        widgets = {
            'date': forms.DateInput()
        }


class NumberPlantForm(forms.Form):
    number_of_plants = forms.IntegerField(min_value=1, max_value=100)
