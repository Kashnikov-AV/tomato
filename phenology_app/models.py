from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class Tk(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200, null=True, blank=True)

    def get_blocks_list_url(self):
        return reverse('phenology:blocks-list', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name}'


class Block(models.Model):
    key = models.PositiveIntegerField(verbose_name='block')
    tk = models.ForeignKey(Tk, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['key', 'tk']]

    def get_absolute_url(self):
        return reverse('phenology:plants-list', kwargs={'pk': self.tk.pk,
                                                        'block': self.key
                                                        })

    def get_records_list_url(self):
        return reverse('phenology:records-list', kwargs={'pk': self.tk.pk,
                                                         'block': self.key
                                                         })

    def __str__(self):
        return f'Тк: {self.tk} Блок: {self.key}'

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            super(Block, self).save(*args, **kwargs)


class Plant(models.Model):
    key = models.PositiveIntegerField(verbose_name='plant')
    block = models.ForeignKey(Block, on_delete=models.CASCADE)

    class Meta:
        unique_together = [["key", "block"]]

    def get_record_create_url(self):
        return reverse('phenology:record-create', kwargs={'pk': self.block.tk.pk,
                                                          'block': self.block.key,
                                                          'plant': self.key
                                                          })

    def __str__(self):
        return f'{self.block} Растение: {self.key}'


class Record(models.Model):
    date = models.DateField(default=now)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='records')

    class Meta:
        unique_together = [["plant", "date"]]

    growth_per_week = models.FloatField(blank=True, null=True, verbose_name='Прирост за неделю')
    stem_diameter = models.FloatField(blank=True, null=True, verbose_name='Диаметр стебля')
    leaf_length = models.FloatField(blank=True, null=True, verbose_name='Длина листа')
    leaf_width = models.FloatField(blank=True, null=True, verbose_name='Ширина листа')
    number_of_leaves_per_stem = models.FloatField(blank=True, null=True, verbose_name='оличество листьев на стебель')
    internode_length = models.FloatField(blank=True, null=True, verbose_name='Длина междоузлия')

    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'pk': self.plant.block.tk.pk,
                                                'block': self.plant.block.pk,
                                                'plant': self.plant.pk,
                                                'record': self.pk
                                                })

    def __str__(self):
        return f'{self.pk}'
