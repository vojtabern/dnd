# Generated by Django 4.2.1 on 2023-06-02 14:46

import django.core.validators
from django.db import migrations, models
import dnd.models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0009_interestingplaces'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interestingplaces',
            options={'ordering': ['nazev'], 'verbose_name': 'Zajímavé místo', 'verbose_name_plural': 'Zajímavá místa'},
        ),
        migrations.AddField(
            model_name='budova',
            name='mapa',
            field=models.ImageField(blank=True, upload_to=dnd.models.get_budova_upload_path, verbose_name='Mapa'),
        ),
        migrations.AddField(
            model_name='interestingplaces',
            name='mapa',
            field=models.ImageField(blank=True, upload_to=dnd.models.get_place_upload_path, verbose_name='Mapa'),
        ),
        migrations.AlterField(
            model_name='interestingplaces',
            name='typ',
            field=models.CharField(choices=[('dungeon', 'Dungeon'), ('jeskyně', 'Jeskyně'), ('place_of_power', 'Místo moci'), ('building', 'Budova')], max_length=20, verbose_name='Typ místa'),
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('nazev', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('dmg_dice', models.CharField(blank=True, help_text='Formát 1k8', max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]+k[0-9]+$', 'Zadej formát s "k".')], verbose_name='Kostky poškození')),
                ('max_dmg', models.IntegerField(blank=True, verbose_name='Maximální možné poškození')),
                ('bonus_to_hit', models.IntegerField(default=0, verbose_name='Bonus k zásahu')),
                ('reach', models.IntegerField(default=0, verbose_name='Dosah')),
                ('desc', models.TextField(verbose_name='Popis')),
                ('npc', models.ManyToManyField(to='dnd.npc', verbose_name='NPC')),
            ],
            options={
                'verbose_name': 'Akce',
                'verbose_name_plural': 'Akce',
                'ordering': ['nazev'],
            },
        ),
    ]
