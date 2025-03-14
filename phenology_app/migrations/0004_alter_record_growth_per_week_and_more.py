# Generated by Django 5.0.2 on 2025-03-06 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phenology_app', '0003_alter_block_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='growth_per_week',
            field=models.FloatField(blank=True, verbose_name='Прирост за неделю'),
        ),
        migrations.AlterField(
            model_name='record',
            name='internode_length',
            field=models.FloatField(blank=True, verbose_name='Длина междоузлия'),
        ),
        migrations.AlterField(
            model_name='record',
            name='leaf_length',
            field=models.FloatField(blank=True, verbose_name='Длина листа'),
        ),
        migrations.AlterField(
            model_name='record',
            name='leaf_width',
            field=models.FloatField(blank=True, verbose_name='Ширина листа'),
        ),
        migrations.AlterField(
            model_name='record',
            name='number_of_leaves_per_stem',
            field=models.FloatField(blank=True, verbose_name='оличество листьев на стебель'),
        ),
        migrations.AlterField(
            model_name='record',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='phenology_app.plant'),
        ),
        migrations.AlterField(
            model_name='record',
            name='stem_diameter',
            field=models.FloatField(blank=True, verbose_name='Диаметр стебля'),
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('plant', 'date')},
        ),
    ]
