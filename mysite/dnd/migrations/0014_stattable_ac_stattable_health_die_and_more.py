# Generated by Django 4.2.1 on 2023-06-02 20:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0013_remove_stat_politicke_usporadani_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stattable',
            name='ac',
            field=models.IntegerField(default=10, verbose_name='Brnění'),
        ),
        migrations.AddField(
            model_name='stattable',
            name='health_die',
            field=models.IntegerField(default=10, verbose_name='Životů'),
        ),
        migrations.AddField(
            model_name='stattable',
            name='roll_health',
            field=models.CharField(blank=True, help_text='Formát 1k8', max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]+k[0-9]+$', 'Zadej formát s "k".')], verbose_name='Kostky životů'),
        ),
        migrations.AddField(
            model_name='stattable',
            name='speed',
            field=models.IntegerField(default=6, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(60)], verbose_name='Rychlost'),
        ),
        migrations.AlterField(
            model_name='stattable',
            name='moudrost',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Moudrost'),
        ),
    ]
