# Generated by Django 4.2.1 on 2023-05-30 16:08

from django.db import migrations, models
import django.db.models.deletion
import dnd.models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budova',
            options={'ordering': ['nazev'], 'verbose_name': 'Budova', 'verbose_name_plural': 'Budovy'},
        ),
        migrations.RemoveField(
            model_name='mesto',
            name='npc_idnpc',
        ),
        migrations.RemoveField(
            model_name='mesto',
            name='typ_mesta_typ',
        ),
        migrations.RemoveField(
            model_name='mesto',
            name='vladce_idvladce',
        ),
        migrations.RemoveField(
            model_name='npc',
            name='changed_filename',
        ),
        migrations.AddField(
            model_name='budova',
            name='vlastnik',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dnd.npc'),
        ),
        migrations.AddField(
            model_name='mesto',
            name='spravce',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dnd.vladce', verbose_name='Správce města'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mesto',
            name='typ_mesta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dnd.typmesta', verbose_name='Typ města'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npc',
            name='mesto',
            field=models.ManyToManyField(to='dnd.mesto'),
        ),
        migrations.AlterField(
            model_name='budova',
            name='mesto_nazev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnd.mesto', verbose_name='Město'),
        ),
        migrations.AlterField(
            model_name='budova',
            name='typ_budovy',
            field=models.CharField(choices=[('inn', 'Hospoda (inn)'), ('church', 'Kostel (church)'), ('market', 'Tržiště (market)'), ('guild', 'Cech (guild)'), ('temple', 'Chrám (temple)'), ('library', 'Knihovna (library)'), ('castle', 'Hrad (castle)'), ('blacksmith', 'Kovárna (blacksmith)'), ('shop', 'Obchod (shop)'), ('magic_shop', 'Obchod s magickými předměty (magic shop)')], max_length=50, verbose_name='Typ budovy'),
        ),
        migrations.RemoveField(
            model_name='mesto',
            name='opevneni_typ',
        ),
        migrations.AlterField(
            model_name='mesto',
            name='stat_nazev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnd.stat', verbose_name='Stát'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='fotka',
            field=models.ImageField(blank=True, upload_to=dnd.models.get_npc_upload_path, verbose_name='Fotka'),
        ),
        migrations.AddField(
            model_name='mesto',
            name='opevneni_typ',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='dnd.opevneni', verbose_name='Typ opevnění'),
            preserve_default=False,
        ),
    ]
