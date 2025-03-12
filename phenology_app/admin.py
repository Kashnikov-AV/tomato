from django.contrib import admin
from .models import *


class TkAdmin(admin.ModelAdmin):
    model = Tk
    list_display = ('pk', 'name')
admin.site.register(Tk, TkAdmin)


class BlockAdmin(admin.ModelAdmin):
    model = Block
    list_display = ('key', 'tk', 'pk')
admin.site.register(Block, BlockAdmin)


class PlantAdmin(admin.ModelAdmin):
    model = Plant
    list_display = ('block', 'key', 'pk')
admin.site.register(Plant, PlantAdmin)


class RecordAdmin(admin.ModelAdmin):
    model = Record
    list_display = ('pk', 'date', 'growth_per_week', 'stem_diameter', 'leaf_length', 'leaf_width', 'number_of_leaves_per_stem', 'internode_length')
admin.site.register(Record, RecordAdmin)
