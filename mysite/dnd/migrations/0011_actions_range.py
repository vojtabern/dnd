# Generated by Django 4.2.1 on 2023-06-02 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0010_alter_interestingplaces_options_budova_mapa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='range',
            field=models.CharField(blank=True, help_text='Formát 4/6', max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]+/[0-9]+$', 'Zadej formát s "/".')], verbose_name='Dosah na dálku'),
        ),
    ]
