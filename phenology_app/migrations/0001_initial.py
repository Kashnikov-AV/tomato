# Generated by Django 5.0.2 on 2025-03-01 20:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.PositiveIntegerField(verbose_name='number')),
            ],
        ),
        migrations.CreateModel(
            name='Tk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.PositiveIntegerField(verbose_name='plant')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenology_app.block')),
            ],
            options={
                'unique_together': {('key', 'block')},
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('growth_per_week', models.FloatField(default=0.0)),
                ('stem_diameter', models.FloatField(default=0.0)),
                ('leaf_length', models.FloatField(default=0.0)),
                ('leaf_width', models.FloatField(default=0.0)),
                ('number_of_leaves_per_stem', models.FloatField(default=0.0)),
                ('internode_length', models.FloatField(default=0.0)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenology_app.plant')),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='tk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenology_app.tk'),
        ),
        migrations.AlterUniqueTogether(
            name='block',
            unique_together={('key', 'tk')},
        ),
    ]
