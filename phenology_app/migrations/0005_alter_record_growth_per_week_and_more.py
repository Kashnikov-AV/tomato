# Generated by Django 5.0.2 on 2025-03-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phenology_app', '0004_alter_record_growth_per_week_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='growth_per_week',
            field=models.FloatField(blank=True, null=True, verbose_name='Прирост за неделю'),
        ),
        migrations.AlterField(
            model_name='record',
            name='internode_length',
            field=models.FloatField(blank=True, null=True, verbose_name='Длина междоузлия'),
        ),
        migrations.AlterField(
            model_name='record',
            name='leaf_length',
            field=models.FloatField(blank=True, null=True, verbose_name='Длина листа'),
        ),
        migrations.AlterField(
            model_name='record',
            name='leaf_width',
            field=models.FloatField(blank=True, null=True, verbose_name='Ширина листа'),
        ),
        migrations.AlterField(
            model_name='record',
            name='number_of_leaves_per_stem',
            field=models.FloatField(blank=True, null=True, verbose_name='оличество листьев на стебель'),
        ),
        migrations.AlterField(
            model_name='record',
            name='stem_diameter',
            field=models.FloatField(blank=True, null=True, verbose_name='Диаметр стебля'),
        ),
    ]
